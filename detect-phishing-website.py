from joblib import load
import numpy as np

# Load the model
model = load('phishing_website_detector.joblib')

# Initialize sample data
X = np.array([[-0.16505472159476944,-0.19396371681162317,-0.4210204437176671,-1.0811360640123888,0.001173789773179425,-0.14291456824952412,-0.3874640948980485,-0.1976037016602993,-0.2936828780275021,-0.2951278279995703,-0.08181489007173054,-0.08394589397130167,-0.15385908829247383,-0.02646512292755605,-0.11613514861427882,-0.038983834787668294,-0.10413912316872789,-0.024962057112744924,-0.09271679140121629,-0.8935594992888882,-0.3377294035229024,-0.08127127300011637,-0.09867344059710981,-1.2531049810555424,-0.5946509071652016,-0.2678684239204823,-0.018710391971381506,-0.04866002412564594,-0.26499947000158997,-0.22973247533559277,-0.14861728192150897,-1.933425413670506,1.9848170453579965,-0.30142500524189014,-0.3752764559695032,-0.013229087286639308,-0.7201430940803879,-0.05620994273193427,-0.5801765604836449,-0.6138895051757202,2.655560014391947,2.532148164551768,2.202054683618349,-0.01783641267397378,0.9189387247768576,0.10566835037640751,1.2240438968741663,2.0462147467506657,0.8266115349293433,-0.38897250634143393,-0.3410571112298085,-0.06425701708705941,-0.07016772590799636,-0.1351399505552676,-0.18039163159577684,-0.3969378307811771,0.9295158708489617,-0.7160663186471066,-0.28450709896584675,3.1568852074976212,-0.3999224747655696,-0.2606240220595968,-0.8903145370631085,1.1565571794264193,1.2352904525877677,-0.6053498794718896,-0.036249971679720695,-0.07793207960073419,1.3548453470711344,-0.033743931099489914,-0.03744044976733646,-0.37754864958952933,0.5374978364811542,-0.8855872355647364,-0.28036967198293944,0.7050987982625174,0.9346153904688635,-0.3701221315451759,-0.1433028760552777,-1.0703611477775492,0.7151643578821109],
[1.100884835796812,-0.3795492921637788,-0.4210204437176671,9.870756294919609,0.48033154361036096,-0.14291456824952412,-0.3874640948980485,-0.1976037016602993,-0.2936828780275021,0.619544372118404,-0.08181489007173054,-0.08394589397130167,-0.6851610155380862,-0.02646512292755605,-0.11613514861427882,-0.038983834787668294,-0.10413912316872789,-0.024962057112744924,-0.09271679140121629,1.0989073514469665,2.300853701239076,-0.08127127300011637,5.806234549062394,0.7980177360380919,-0.04428184900445839,-0.2678684239204823,-0.018710391971381506,-0.04866002412564594,-0.26499947000158997,-0.22973247533559277,-0.14861728192150897,1.2060904945911626,-0.5038247743482234,-0.30142500524189014,-0.3752764559695032,-0.013229087286639308,-0.7201430940803879,-0.05620994273193427,2.2912664148417585,0.4346083048357083,-0.5097488385168005,1.263565774137357,-0.13308640632603932,-0.24425822171830996,-0.09489012256194686,-0.06766535295343429,-0.6083587714598209,0.6488946341063891,-0.09066798620086469,0.7978816707761821,-0.3410571112298085,-0.06425701708705941,14.25156632995626,-0.1351399505552676,-0.18039163159577684,-0.3549590616058798,0.10731580031844826,0.2513641120083241,-0.28450709896584675,3.1568852074976212,0.24027482840488457,-0.2606240220595968,-0.8903145370631085,1.1565571794264193,1.2352904525877677,-0.6053498794718896,-0.036249971679720695,-0.07793207960073419,-0.9486135646085243,-0.033743931099489914,-0.03744044976733646,-0.37754864958952933,0.5374978364811542,1.1291942338829022,3.566719584637706,-0.6045314586039304,-1.307594327280023,-0.4293403180928934,-0.1433028760552777,0.9342641052287407,-1.2557881932565609],
[-0.599091141271883,-0.10117092913554535,-0.4210204437176671,-0.3510099067502556,-0.477983964064002,-0.14291456824952412,-0.3874640948980485,-0.1976037016602993,-0.2936828780275021,-0.2951278279995703,-0.08181489007173054,-0.08394589397130167,-0.6851610155380862,-0.02646512292755605,-0.11613514861427882,-0.038983834787668294,-0.10413912316872789,-0.024962057112744924,-0.09271679140121629,1.0989073514469665,-0.3377294035229024,-0.08127127300011637,-0.09867344059710981,0.7980177360380919,-0.5946509071652016,-0.2678684239204823,-0.018710391971381506,-0.04866002412564594,-0.26499947000158997,-0.22973247533559277,-0.14861728192150897,-0.3636674595396717,-0.5038247743482234,-0.30142500524189014,-0.3752764559695032,-0.013229087286639308,0.7252011667341571,-0.05620994273193427,-0.7596417464414825,0.015209180831136912,-0.057561859529836584,-0.512449572442819,-0.8002695748815788,-0.15368949810057547,0.31064141637357495,-0.4576661854455783,0.05816182994140343,-0.049765422215749006,-0.7125524072017403,-0.38897250634143393,-0.3410571112298085,-0.06425701708705941,-0.07016772590799636,-0.1351399505552676,-0.18039163159577684,-0.3789469297060497,-0.8255650500100787,1.3490255634373018,0.0779849466455264,-0.15493476761928632,-0.0233358284778796,3.836944852962674,1.1231985532873723,-0.6497434579622988,-0.926971135238113,1.9998413997900857,-0.036249971679720695,-0.07793207960073419,-0.6926736855330067,-0.033743931099489914,-0.03744044976733646,-0.37754864958952933,0.5374978364811542,1.1291942338829022,-0.28036967198293944,0.5909510814034925,-0.44552776099855523,0.22646109579276513,-0.1433028760552777,-1.0703611477775492,0.3209738476543765],
])

# Make predictions
predictions = model.predict(X)
print("Result must be [-1.0, 1.0, -1.0]")
print(predictions)