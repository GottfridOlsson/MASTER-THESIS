EC-LAB SETTING FILE

Number of linked techniques : 8

EC-LAB for windows v11.46 (software)
Internet server v11.40 (firmware)
Command interpretor v11.40 (firmware)

Filename : C:\Users\kmf\Desktop\Biologic Data\Gottfrid\2024-04-03_CTTA-01-02\2024-04-03_CTTA_03-0.050mAhcm2.mps

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
Electrode surface area : 0.001 cm�
Characteristic mass : 0.001 g
Equivalent Weight : 0.000 g/eq.
Density : 0.000 g/cm3
Volume (V) : 0.001 cm�
Cycle Definition : Charge/Discharge alternance
Do not turn to OCV between techniques

Technique : 1
Open Circuit Voltage
tR (h:m:s)          0:01:0.0000         
dER/dt (mV/h)       0.0                 
record              <Ewe>               
dER (mV)            5.00                
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
unit dI             �A                  
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
unit Is             �A                  
vs.                 <None>              
ts (h:m:s)          0:03:0.0000         
EM (V)              pass                
dQM                 9.800               
unit dQM            �A.h                
record              Ewe                 
dEs (mV)            1.00                
dts (s)             1.0000              
E range min (V)     -5.000              
E range max (V)     5.000               
I Range             100 �A              
Bandwidth           5                   
goto Ns'            0                   
nc cycles           0                   

Technique : 4
Modulo Bat
ctrl_type           Rest                
Apply I/C           I                   
current/potential   current             
ctrl1_val           1.000               
ctrl1_val_unit                          
ctrl1_val_vs                            
ctrl2_val           0.000               
ctrl2_val_unit                          
ctrl2_val_vs                            
ctrl3_val           0.000               
ctrl3_val_unit                          
ctrl3_val_vs                            
N                   0.00                
charge/discharge    Charge              
charge/discharge_1  Charge              
Apply I/C_1         I                   
N1                  0.00                
ctrl4_val           0.000               
ctrl4_val_unit                          
ctrl_seq            0                   
ctrl_repeat         0                   
ctrl_trigger        Falling Edge        
ctrl_TO_t           0.000               
ctrl_TO_t_unit      d                   
ctrl_Nd             6                   
ctrl_Na             2                   
ctrl_corr           0                   
lim_nb              2                   
lim1_type           Ewe                 
lim1_comp           >                   
lim1_Q              Q limit             
lim1_value          0.050               
lim1_value_unit     V                   
lim1_action         Next sequence       
lim1_seq            1                   
lim2_type           Time                
lim2_comp           >                   
lim2_Q              Q limit             
lim2_value          100.000             
lim2_value_unit     h                   
lim2_action         Next sequence       
lim2_seq            1                   
rec_nb              2                   
rec1_type           Ewe                 
rec1_value          1.000               
rec1_value_unit     mV                  
rec2_type           Time                
rec2_value          30.000              
rec2_value_unit     s                   
E range min (V)     -5.000              
E range max (V)     5.000               
I Range             10 mA               
I Range min         Unset               
I Range max         Unset               
I Range init        Unset               
auto rest           0                   
Bandwidth           5                   

Technique : 5
Chronopotentiometry
Is                  -196.000            
unit Is             �A                  
vs.                 <None>              
ts (h:m:s)          0:06:0.0000         
EM (V)              pass                
dQM                 19.600              
unit dQM            �A.h                
record              Ewe                 
dEs (mV)            1.00                
dts (s)             1.0000              
E range min (V)     -5.000              
E range max (V)     5.000               
I Range             100 �A              
Bandwidth           5                   
goto Ns'            0                   
nc cycles           0                   

Technique : 6
Modulo Bat
ctrl_type           Rest                
Apply I/C           I                   
current/potential   current             
ctrl1_val           1.000               
ctrl1_val_unit                          
ctrl1_val_vs                            
ctrl2_val           0.000               
ctrl2_val_unit                          
ctrl2_val_vs                            
ctrl3_val           0.000               
ctrl3_val_unit                          
ctrl3_val_vs                            
N                   0.00                
charge/discharge    Charge              
charge/discharge_1  Charge              
Apply I/C_1         I                   
N1                  0.00                
ctrl4_val           0.000               
ctrl4_val_unit                          
ctrl_seq            0                   
ctrl_repeat         0                   
ctrl_trigger        Falling Edge        
ctrl_TO_t           0.000               
ctrl_TO_t_unit      d                   
ctrl_Nd             6                   
ctrl_Na             2                   
ctrl_corr           0                   
lim_nb              2                   
lim1_type           Ewe                 
lim1_comp           >                   
lim1_Q              Q limit             
lim1_value          0.050               
lim1_value_unit     V                   
lim1_action         Next sequence       
lim1_seq            1                   
lim2_type           Time                
lim2_comp           >                   
lim2_Q              Q limit             
lim2_value          100.000             
lim2_value_unit     h                   
lim2_action         Next sequence       
lim2_seq            1                   
rec_nb              2                   
rec1_type           Ewe                 
rec1_value          1.000               
rec1_value_unit     mV                  
rec2_type           Time                
rec2_value          1.000               
rec2_value_unit     s                   
E range min (V)     -5.000              
E range max (V)     5.000               
I Range             10 mA               
I Range min         Unset               
I Range max         Unset               
I Range init        Unset               
auto rest           0                   
Bandwidth           5                   

Technique : 7
Chronopotentiometry
Is                  -196.000            
unit Is             �A                  
vs.                 <None>              
ts (h:m:s)          0:30:0.0000         
EM (V)              pass                
dQM                 98.000              
unit dQM            �A.h                
record              Ewe                 
dEs (mV)            1.00                
dts (s)             5.0000              
E range min (V)     -5.000              
E range max (V)     5.000               
I Range             100 �A              
Bandwidth           5                   
goto Ns'            0                   
nc cycles           0                   

Technique : 8
Modulo Bat
ctrl_type           Rest                
Apply I/C           I                   
current/potential   current             
ctrl1_val           0.000               
ctrl1_val_unit                          
ctrl1_val_vs                            
ctrl2_val           0.000               
ctrl2_val_unit                          
ctrl2_val_vs                            
ctrl3_val           0.000               
ctrl3_val_unit                          
ctrl3_val_vs                            
N                   0.00                
charge/discharge    Charge              
charge/discharge_1  Charge              
Apply I/C_1         I                   
N1                  0.00                
ctrl4_val           0.000               
ctrl4_val_unit                          
ctrl_seq            0                   
ctrl_repeat         0                   
ctrl_trigger        Falling Edge        
ctrl_TO_t           0.000               
ctrl_TO_t_unit      d                   
ctrl_Nd             6                   
ctrl_Na             2                   
ctrl_corr           0                   
lim_nb              2                   
lim1_type           Ewe                 
lim1_comp           >                   
lim1_Q              Q limit             
lim1_value          0.050               
lim1_value_unit     V                   
lim1_action         Next sequence       
lim1_seq            1                   
lim2_type           Time                
lim2_comp           >                   
lim2_Q              Q limit             
lim2_value          100.000             
lim2_value_unit     s                   
lim2_action         Next sequence       
lim2_seq            1                   
rec_nb              2                   
rec1_type           Ewe                 
rec1_value          1.000               
rec1_value_unit     mV                  
rec2_type           Time                
rec2_value          1.000               
rec2_value_unit     s                   
E range min (V)     -5.000              
E range max (V)     5.000               
I Range             10 mA               
I Range min         Unset               
I Range max         Unset               
I Range init        Unset               
auto rest           0                   
Bandwidth           5                   
