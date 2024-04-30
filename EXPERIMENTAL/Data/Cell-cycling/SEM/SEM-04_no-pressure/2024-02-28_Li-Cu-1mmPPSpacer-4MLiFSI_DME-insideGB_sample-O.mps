EC-LAB SETTING FILE

Number of linked techniques : 3

EC-LAB for windows v11.46 (software)
Internet server v11.40 (firmware)
Command interpretor v11.40 (firmware)

Filename : C:\Users\kmf\Desktop\Biologic Data\Gottfrid\SEM-04_no-pressure\2024-02-28_Li-Cu-1mmPPSpacer-4MLiFSI_DME-insideGB_sample-O.mps

Device : VMP3
CE vs. WE compliance from -10 V to 10 V
Electrode connection : standard
Potential control : Ewe
Ewe ctrl range : min = -5.00 V, max = 5.00 V
Safety Limits :
	Do not start on E overload
Electrode material : 
Initial state : 
Electrolyte : 
Comments : 
Electrode surface area : 0.001 cm²
Characteristic mass : 0.001 g
Equivalent Weight : 0.000 g/eq.
Density : 0.000 g/cm3
Volume (V) : 0.001 cm³
Cycle Definition : Charge/Discharge alternance
Turn to OCV between techniques

Technique : 1
Open Circuit Voltage
tR (h:m:s)          0:01:0.0000         
dER/dt (mV/h)       0.0                 
record              <Ewe>               
dER (mV)            0.00                
dtR (s)             10.0000             
E range min (V)     -5.000              
E range max (V)     5.000               

Technique : 2
Chronoamperometry / Chronocoulometry
Ei (V)              0.010               
vs.                 Ref                 
ti (h:m:s)          0:15:0.0000         
Imax                pass                
unit Imax           mA                  
Imin                pass                
unit Imin           mA                  
dQM                 0.000               
unit dQM            mA.h                
record              <I>                 
dI                  5.000               
unit dI             µA                  
dQ                  0.000               
unit dQ             mA.h                
dt (s)              0.1000              
dta (s)             1.0000              
E range min (V)     -5.000              
E range max (V)     5.000               
I Range             Auto                
I Range min         Unset               
I Range max         Unset               
I Range init        Unset               
Bandwidth           5                   
goto Ns'            0                   
nc cycles           0                   

Technique : 3
Chronopotentiometry
Is                  -196.000            
unit Is             µA                  
vs.                 <None>              
ts (h:m:s)          0:00:36.0000        
EM (V)              pass                
dQM                 1.960               
unit dQM            µA.h                
record              Ewe                 
dEs (mV)            1.00                
dts (s)             0.0100              
E range min (V)     -5.000              
E range max (V)     5.000               
I Range             100 µA              
Bandwidth           5                   
goto Ns'            0                   
nc cycles           0                   
