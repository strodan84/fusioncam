flowchart LR

%% =======================
%% Fusion Environment
%% =======================
A[Fusion Plasma Environment\nHeat flux • Radiation • Magnetic field • Impurities]

B[Plasma-Facing Components\nDivertor / First Wall / Liquid Metal Surface]

A --> B

%% =======================
%% Optical System
%% =======================
B --> C[Optical Collection System\nSapphire viewport + lenses + spectral filters]

C --> D[Radiation & Magnetic Shielding\nNeutron/gamma attenuation + EM shielding + thermal isolation]

D --> E[Multispectral Sensor Module\nCMOS visible + IR thermography + calibration sources]

E --> F[Edge Processing Unit\nFPGA/CPU\nFrame filtering + event detection + compression]

F --> G[Data System / Shot Archive\nTime sync + storage + analysis pipeline + ML detection]

%% =======================
%% Styling (important for “publication feel”)
%% =======================

classDef env fill:#1f2937,stroke:#9ca3af,color:#ffffff;
classDef plasma fill:#111827,stroke:#60a5fa,color:#ffffff;
classDef optics fill:#0f172a,stroke:#f59e0b,color:#ffffff;
classDef shield fill:#111827,stroke:#ef4444,color:#ffffff;
classDef sensor fill:#0f172a,stroke:#22c55e,color:#ffffff;
classDef compute fill:#0b1220,stroke:#a855f7,color:#ffffff;
classDef data fill:#020617,stroke:#38bdf8,color:#ffffff;

class A env;
class B plasma;
class C optics;
class D shield;
class E sensor;
class F compute;
class G data;