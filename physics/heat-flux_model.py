'''
This model aims to do three things:
    1. Convert incident heat flux → surface temperature evolution
    2. Include a simple energy balance model
    3. Provide a bridge to what the camera would actually observe
'''

# physics/heat_flux_model.py

import numpy as np

sigma = 5.670374419e-8  # Stefan-Boltzmann constant (W/m^2/K^4)


def surface_energy_balance(
    q_in,
    T0,
    t,
    rho=19300,        # tungsten (W) density (kg/m^3) - typical PFC material
    Cp=134,           # J/(kg K)
    thickness=0.005,  # 5 mm tile
    emissivity=0.3
):
    """
    Simple 1D lumped thermal model for a plasma-facing component.

    Governing equation:
        rho * Cp * dT/dt = q_in - q_rad

    where:
        q_rad = emissivity * sigma * T^4

    Parameters
    ----------
    q_in : float or ndarray
        incident heat flux (W/m^2), assumed constant or time-dependent
    T0 : float
        initial temperature (K)
    t : ndarray
        time array (s)
    rho : float
        material density (kg/m^3)
    Cp : float
        heat capacity (J/kg/K)
    thickness : float
        effective thickness of heated layer (m)
    emissivity : float
        surface emissivity

    Returns
    -------
    T : ndarray
        surface temperature evolution (K)
    """

    dt = np.diff(t)
    T = np.zeros_like(t)
    T[0] = T0

    areal_heat_capacity = rho * Cp * thickness  # J/m^2/K

    for i in range(1, len(t)):

        # radiative losses
        q_rad = emissivity * sigma * T[i-1]**4

        # net heat flux
        q_net = q_in - q_rad

        # explicit Euler update
        dT = (q_net / areal_heat_capacity) * dt[i-1]

        T[i] = T[i-1] + dT

        # physical constraint (no negative temps)
        T[i] = max(T[i], 0.0)

    return T


def steady_state_temperature(q_in, emissivity=0.3):
    """
    Solve approximate steady-state temperature:
        q_in = emissivity * sigma * T^4
    """

    return (q_in / (emissivity * sigma)) ** 0.25


def demo_heat_pulse():
    """
    Generate a simple fusion-relevant heat pulse scenario.

    Example:
    - plasma shot lasting ~0.5 seconds
    - heat flux ramp up and down
    """

    t = np.linspace(0, 1.0, 500)

    # simple pulse shape (Gaussian-like)
    q_peak = 5e6  # 5 MW/m^2 (typical divertor scale)
    q_in = q_peak * np.exp(-((t - 0.5)**2) / 0.02)

    T0 = 500  # initial wall temp (K)

    T = surface_energy_balance(q_in, T0, t)

    return t, q_in, T