import numpy as np

def collection_solid_angle(aperture_diameter, distance):
    """
    Approximate collection solid angle of a circular aperture.

    Parameters:
    -----------

    aperture_diameter : float
        Lens diameter (m)

    distance : float
        Distance from target (m)

    Returns:    
    --------
    float
        Solid angle (steradians)
    """

    radius = aperture_diameter / 2

    return np.pi * radius**2 / distance**2



def optical_throughput(
    lens_transmission=0.95,
    viewport_transmission=0.90,
    filter_transmission=0.80
):
    """
    Overall transmission efficiency.
    """

    return (
        lens_transmission *
        viewport_transmission *
        filter_transmission
    )


"""
Collected Optical Power
Now combine geometry and throughput.
"""

def collected_power(
    emitted_power_density,
    target_area,
    aperture_diameter,
    distance,
    throughput=0.70
):
    """
    Estimate optical power entering the camera.

    Parameters
    ----------
    emitted_power_density : float or ndarray
        Radiated power density (W/m²)

    target_area : float
        Observed emitting area (m²)

    aperture_diameter : float
        Lens diameter (m)

    distance : float
        Camera distance (m)
    """

    omega = collection_solid_angle(
        aperture_diameter,
        distance
    )

    return (
        emitted_power_density *
        target_area *
        omega /
        (4*np.pi)
    ) * throughput