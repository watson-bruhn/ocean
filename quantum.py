from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
linear = {('x0', 'x0'): -18.916080, ('x1', 'x1'): -18.995626, ('x2', 'x2'): -18.939288, ('x3', 'x3'): -18.924209, ('x4', 'x4'): -18.997967, ('x5', 'x5'): -18.995744, ('x6', 'x6'): -18.958683, ('x7', 'x7'): -18.894051, ('x8', 'x8'): -18.966814, ('x9', 'x9'): -18.828014, ('x10', 'x10'): -18.796004, ('x11', 'x11'): -18.933918, ('x12', 'x12'): -18.993252, ('x13', 'x13'): -18.996008, ('x14', 'x14'): -18.973813, ('x15', 'x15'): -18.905784, ('x16', 'x16'): -18.998964, ('x17', 'x17'): -18.999316, ('x18', 'x18'): -18.972330, ('x19', 'x19'): -18.520857, ('x20', 'x20'): -18.973181, ('x21', 'x21'): -18.986155, ('x22', 'x22'): -18.998890, ('x23', 'x23'): -18.734346, ('x24', 'x24'): -18.983698, ('x25', 'x25'): -18.943464, ('x26', 'x26'): -18.819363, ('x27', 'x27'): -18.964567, ('x28', 'x28'): -18.931055, ('x29', 'x29'): -18.890527, ('x30', 'x30'): -18.947559, ('x31', 'x31'): -18.984399, ('x32', 'x32'): -18.997866, ('x33', 'x33'): -18.923434, ('x34', 'x34'): -18.810622, ('x35', 'x35'): -18.854975, ('x36', 'x36'): -18.983117, ('x37', 'x37'): -18.979252, ('x38', 'x38'): -18.996617, ('x39', 'x39'): -18.998448, ('x40', 'x40'): -18.918208, ('x41', 'x41'): -18.943817, ('x42', 'x42'): -18.572924, ('x43', 'x43'): -18.744789, ('x44', 'x44'): -18.939099, ('x45', 'x45'): -18.969029, ('x46', 'x46'): -18.534441, ('x47', 'x47'): -18.500000, ('x48', 'x48'): -18.671593, ('x49', 'x49'): -18.998691}
quadratic = {('x0', 'x1'): 1.961683, ('x0', 'x2'): 2.142758, ('x0', 'x3'): 2.159504, ('x0', 'x4'): 2.026125, ('x0', 'x5'): 2.037798, ('x0', 'x6'): 1.882231, ('x0', 'x7'): 2.188588, ('x0', 'x8'): 2.105546, ('x0', 'x9'): 1.759724, ('x0', 'x10'): 2.261682, ('x0', 'x11'): 2.148938, ('x0', 'x12'): 2.047594, ('x0', 'x13'): 1.963396, ('x0', 'x14'): 2.093758, ('x0', 'x15'): 2.177839, ('x0', 'x16'): 2.018645, ('x0', 'x17'): 1.984846, ('x0', 'x18'): 2.096375, ('x0', 'x19'): 2.401048, ('x0', 'x20'): 2.094882, ('x0', 'x21'): 2.068173, ('x0', 'x22'): 2.019306, ('x0', 'x23'): 2.298622, ('x0', 'x24'): 2.073975, ('x0', 'x25'): 2.137761, ('x0', 'x26'): 1.753755, ('x0', 'x27'): 2.109061, ('x0', 'x28'): 2.152130, ('x0', 'x29'): 1.808302, ('x0', 'x30'): 2.132678, ('x0', 'x31'): 2.072366, ('x0', 'x32'): 2.026763, ('x0', 'x33'): 1.839682, ('x0', 'x34'): 2.252132, ('x0', 'x35'): 1.779360, ('x0', 'x36'): 1.924719, ('x0', 'x37'): 2.083456, ('x0', 'x38'): 1.966300, ('x0', 'x39'): 1.977176, ('x0', 'x40'): 2.165699, ('x0', 'x41'): 2.137330, ('x0', 'x42'): 2.378631, ('x0', 'x43'): 2.292694, ('x0', 'x44'): 1.857020, ('x0', 'x45'): 2.101963, ('x0', 'x46'): 2.395322, ('x0', 'x47'): 2.409684, ('x0', 'x48'): 2.332024, ('x0', 'x49'): 1.979036, ('x1', 'x2'): 1.967410, ('x1', 'x3'): 1.963586, ('x1', 'x4'): 1.994036, ('x1', 'x5'): 1.991371, ('x1', 'x6'): 2.026886, ('x1', 'x7'): 1.956947, ('x1', 'x8'): 1.975905, ('x1', 'x9'): 2.054853, ('x1', 'x10'): 1.940260, ('x1', 'x11'): 1.965999, ('x1', 'x12'): 1.989135, ('x1', 'x13'): 2.008356, ('x1', 'x14'): 1.978596, ('x1', 'x15'): 1.959401, ('x1', 'x16'): 1.995744, ('x1', 'x17'): 2.003459, ('x1', 'x18'): 1.977998, ('x1', 'x19'): 1.908444, ('x1', 'x20'): 1.978339, ('x1', 'x21'): 1.984437, ('x1', 'x22'): 1.995593, ('x1', 'x23'): 1.931827, ('x1', 'x24'): 1.983112, ('x1', 'x25'): 1.968550, ('x1', 'x26'): 2.056216, ('x1', 'x27'): 1.975102, ('x1', 'x28'): 1.965270, ('x1', 'x29'): 2.043763, ('x1', 'x30'): 1.969711, ('x1', 'x31'): 1.983479, ('x1', 'x32'): 1.993890, ('x1', 'x33'): 2.036599, ('x1', 'x34'): 1.942440, ('x1', 'x35'): 2.050370, ('x1', 'x36'): 2.017186, ('x1', 'x37'): 1.980948, ('x1', 'x38'): 2.007694, ('x1', 'x39'): 2.005210, ('x1', 'x40'): 1.962172, ('x1', 'x41'): 1.968649, ('x1', 'x42'): 1.913562, ('x1', 'x43'): 1.933180, ('x1', 'x44'): 2.032641, ('x1', 'x45'): 1.976723, ('x1', 'x46'): 1.909751, ('x1', 'x47'): 1.906472, ('x1', 'x48'): 1.924201, ('x1', 'x49'): 2.004786, ('x2', 'x3'): 2.135667, ('x2', 'x4'): 2.022221, ('x2', 'x5'): 2.032150, ('x2', 'x6'): 1.899831, ('x2', 'x7'): 2.160404, ('x2', 'x8'): 2.089773, ('x2', 'x9'): 1.795632, ('x2', 'x10'): 2.222575, ('x2', 'x11'): 2.126680, ('x2', 'x12'): 2.040482, ('x2', 'x13'): 1.968866, ('x2', 'x14'): 2.079747, ('x2', 'x15'): 2.151262, ('x2', 'x16'): 2.015858, ('x2', 'x17'): 1.987111, ('x2', 'x18'): 2.081973, ('x2', 'x19'): 2.341113, ('x2', 'x20'): 2.080703, ('x2', 'x21'): 2.057985, ('x2', 'x22'): 2.016421, ('x2', 'x23'): 2.253994, ('x2', 'x24'): 2.062920, ('x2', 'x25'): 2.117174, ('x2', 'x26'): 1.790555, ('x2', 'x27'): 2.092762, ('x2', 'x28'): 2.129395, ('x2', 'x29'): 1.836950, ('x2', 'x30'): 2.112850, ('x2', 'x31'): 2.061551, ('x2', 'x32'): 2.022763, ('x2', 'x33'): 1.863641, ('x2', 'x34'): 2.214453, ('x2', 'x35'): 1.812333, ('x2', 'x36'): 1.935970, ('x2', 'x37'): 2.070984, ('x2', 'x38'): 1.971336, ('x2', 'x39'): 1.980587, ('x2', 'x40'): 2.140936, ('x2', 'x41'): 2.116807, ('x2', 'x42'): 2.322046, ('x2', 'x43'): 2.248952, ('x2', 'x44'): 1.878388, ('x2', 'x45'): 2.086725, ('x2', 'x46'): 2.336243, ('x2', 'x47'): 2.348459, ('x2', 'x48'): 2.282405, ('x2', 'x49'): 1.982169, ('x3', 'x4'): 2.024828, ('x3', 'x5'): 2.035921, ('x3', 'x6'): 1.888081, ('x3', 'x7'): 2.179220, ('x3', 'x8'): 2.100303, ('x3', 'x9'): 1.771659, ('x3', 'x10'): 2.248685, ('x3', 'x11'): 2.141540, ('x3', 'x12'): 2.045230, ('x3', 'x13'): 1.965214, ('x3', 'x14'): 2.089101, ('x3', 'x15'): 2.169006, ('x3', 'x16'): 2.017719, ('x3', 'x17'): 1.985599, ('x3', 'x18'): 2.091588, ('x3', 'x19'): 2.381128, ('x3', 'x20'): 2.090169, ('x3', 'x21'): 2.064787, ('x3', 'x22'): 2.018347, ('x3', 'x23'): 2.283789, ('x3', 'x24'): 2.070301, ('x3', 'x25'): 2.130919, ('x3', 'x26'): 1.765986, ('x3', 'x27'): 2.103644, ('x3', 'x28'): 2.144574, ('x3', 'x29'): 1.817824, ('x3', 'x30'): 2.126088, ('x3', 'x31'): 2.068771, ('x3', 'x32'): 2.025433, ('x3', 'x33'): 1.847645, ('x3', 'x34'): 2.239609, ('x3', 'x35'): 1.790319, ('x3', 'x36'): 1.928458, ('x3', 'x37'): 2.079311, ('x3', 'x38'): 1.967974, ('x3', 'x39'): 1.978310, ('x3', 'x40'): 2.157469, ('x3', 'x41'): 2.130509, ('x3', 'x42'): 2.359824, ('x3', 'x43'): 2.278155, ('x3', 'x44'): 1.864122, ('x3', 'x45'): 2.096899, ('x3', 'x46'): 2.375686, ('x3', 'x47'): 2.389335, ('x3', 'x48'): 2.315532, ('x3', 'x49'): 1.980077, ('x4', 'x5'): 2.005884, ('x4', 'x6'): 1.981669, ('x4', 'x7'): 2.029355, ('x4', 'x8'): 2.016429, ('x4', 'x9'): 1.962600, ('x4', 'x10'): 2.040732, ('x4', 'x11'): 2.023183, ('x4', 'x12'): 2.007408, ('x4', 'x13'): 1.994302, ('x4', 'x14'): 2.014594, ('x4', 'x15'): 2.027682, ('x4', 'x16'): 2.002902, ('x4', 'x17'): 1.997641, ('x4', 'x18'): 2.015001, ('x4', 'x19'): 2.062425, ('x4', 'x20'): 2.014769, ('x4', 'x21'): 2.010612, ('x4', 'x22'): 2.003005, ('x4', 'x23'): 2.046482, ('x4', 'x24'): 2.011515, ('x4', 'x25'): 2.021443, ('x4', 'x26'): 1.961671, ('x4', 'x27'): 2.016976, ('x4', 'x28'): 2.023680, ('x4', 'x29'): 1.970161, ('x4', 'x30'): 2.020652, ('x4', 'x31'): 2.011264, ('x4', 'x32'): 2.004166, ('x4', 'x33'): 1.975046, ('x4', 'x34'): 2.039246, ('x4', 'x35'): 1.965656, ('x4', 'x36'): 1.988282, ('x4', 'x37'): 2.012990, ('x4', 'x38'): 1.994754, ('x4', 'x39'): 1.996447, ('x4', 'x40'): 2.025792, ('x4', 'x41'): 2.021376, ('x4', 'x42'): 2.058936, ('x4', 'x43'): 2.045560, ('x4', 'x44'): 1.977744, ('x4', 'x45'): 2.015871, ('x4', 'x46'): 2.061534, ('x4', 'x47'): 2.063770, ('x4', 'x48'): 2.051682, ('x4', 'x49'): 1.996737, ('x5', 'x6'): 1.973478, ('x5', 'x7'): 2.042471, ('x5', 'x8'): 2.023769, ('x5', 'x9'): 1.945889, ('x5', 'x10'): 2.058932, ('x5', 'x11'): 2.033541, ('x5', 'x12'): 2.010718, ('x5', 'x13'): 1.991757, ('x5', 'x14'): 2.021115, ('x5', 'x15'): 2.040050, ('x5', 'x16'): 2.004199, ('x5', 'x17'): 1.996587, ('x5', 'x18'): 2.021704, ('x5', 'x19'): 2.090317, ('x5', 'x20'): 2.021368, ('x5', 'x21'): 2.015353, ('x5', 'x22'): 2.004348, ('x5', 'x23'): 2.067251, ('x5', 'x24'): 2.016659, ('x5', 'x25'): 2.031024, ('x5', 'x26'): 1.944545, ('x5', 'x27'): 2.024561, ('x5', 'x28'): 2.034260, ('x5', 'x29'): 1.956829, ('x5', 'x30'): 2.029880, ('x5', 'x31'): 2.016297, ('x5', 'x32'): 2.006027, ('x5', 'x33'): 1.963896, ('x5', 'x34'): 2.056781, ('x5', 'x35'): 1.950311, ('x5', 'x36'): 1.983047, ('x5', 'x37'): 2.018795, ('x5', 'x38'): 1.992411, ('x5', 'x39'): 1.994860, ('x5', 'x40'): 2.037316, ('x5', 'x41'): 2.030927, ('x5', 'x42'): 2.085269, ('x5', 'x43'): 2.065916, ('x5', 'x44'): 1.967801, ('x5', 'x45'): 2.022962, ('x5', 'x46'): 2.089028, ('x5', 'x47'): 2.092262, ('x5', 'x48'): 2.074773, ('x5', 'x49'): 1.995279, ('x6', 'x7'): 1.867674, ('x6', 'x8'): 1.925942, ('x6', 'x9'): 2.168594, ('x6', 'x10'): 1.816385, ('x6', 'x11'): 1.895495, ('x6', 'x12'): 1.966604, ('x6', 'x13'): 2.025684, ('x6', 'x14'): 1.934213, ('x6', 'x15'): 1.875216, ('x6', 'x16'): 1.986918, ('x6', 'x17'): 2.010633, ('x6', 'x18'): 1.932376, ('x6', 'x19'): 1.718597, ('x6', 'x20'): 1.933424, ('x6', 'x21'): 1.952165, ('x6', 'x22'): 1.986454, ('x6', 'x23'): 1.790466, ('x6', 'x24'): 1.948094, ('x6', 'x25'): 1.903337, ('x6', 'x26'): 2.172782, ('x6', 'x27'): 1.923475, ('x6', 'x28'): 1.893255, ('x6', 'x29'): 2.134509, ('x6', 'x30'): 1.906904, ('x6', 'x31'): 1.949223, ('x6', 'x32'): 1.981221, ('x6', 'x33'): 2.112490, ('x6', 'x34'): 1.823086, ('x6', 'x35'): 2.154816, ('x6', 'x36'): 2.052822, ('x6', 'x37'): 1.941442, ('x6', 'x38'): 2.023647, ('x6', 'x39'): 2.016015, ('x6', 'x40'): 1.883734, ('x6', 'x41'): 1.903640, ('x6', 'x42'): 1.734326, ('x6', 'x43'): 1.794626, ('x6', 'x44'): 2.100324, ('x6', 'x45'): 1.928456, ('x6', 'x46'): 1.722615, ('x6', 'x47'): 1.712538, ('x6', 'x48'): 1.767029, ('x6', 'x49'): 2.014710, ('x7', 'x8'): 2.118592, ('x7', 'x9'): 1.730024, ('x7', 'x10'): 2.294029, ('x7', 'x11'): 2.167348, ('x7', 'x12'): 2.053478, ('x7', 'x13'): 1.958871, ('x7', 'x14'): 2.105348, ('x7', 'x15'): 2.199822, ('x7', 'x16'): 2.020949, ('x7', 'x17'): 1.982973, ('x7', 'x18'): 2.108288, ('x7', 'x19'): 2.450621, ('x7', 'x20'): 2.106611, ('x7', 'x21'): 2.076600, ('x7', 'x22'): 2.021692, ('x7', 'x23'): 2.335535, ('x7', 'x24'): 2.083120, ('x7', 'x25'): 2.154790, ('x7', 'x26'): 1.723317, ('x7', 'x27'): 2.122542, ('x7', 'x28'): 2.170935, ('x7', 'x29'): 1.784606, ('x7', 'x30'): 2.149079, ('x7', 'x31'): 2.081311, ('x7', 'x32'): 2.030071, ('x7', 'x33'): 1.819865, ('x7', 'x34'): 2.283299, ('x7', 'x35'): 1.752086, ('x7', 'x36'): 1.915414, ('x7', 'x37'): 2.093772, ('x7', 'x38'): 1.962134, ('x7', 'x39'): 1.974355, ('x7', 'x40'): 2.186181, ('x7', 'x41'): 2.154305, ('x7', 'x42'): 2.425434, ('x7', 'x43'): 2.328874, ('x7', 'x44'): 1.839346, ('x7', 'x45'): 2.114567, ('x7', 'x46'): 2.444188, ('x7', 'x47'): 2.460325, ('x7', 'x48'): 2.373066, ('x7', 'x49'): 1.976445, ('x8', 'x9'): 1.848904, ('x8', 'x10'): 2.164558, ('x8', 'x11'): 2.093659, ('x8', 'x12'): 2.029930, ('x8', 'x13'): 1.976982, ('x8', 'x14'): 2.058959, ('x8', 'x15'): 2.111833, ('x8', 'x16'): 2.011725, ('x8', 'x17'): 1.990471, ('x8', 'x18'): 2.060605, ('x8', 'x19'): 2.252197, ('x8', 'x20'): 2.059666, ('x8', 'x21'): 2.042870, ('x8', 'x22'): 2.012141, ('x8', 'x23'): 2.187787, ('x8', 'x24'): 2.046519, ('x8', 'x25'): 2.086631, ('x8', 'x26'): 1.845150, ('x8', 'x27'): 2.068582, ('x8', 'x28'): 2.095666, ('x8', 'x29'): 1.879452, ('x8', 'x30'): 2.083434, ('x8', 'x31'): 2.045507, ('x8', 'x32'): 2.016830, ('x8', 'x33'): 1.899185, ('x8', 'x34'): 2.158552, ('x8', 'x35'): 1.861251, ('x8', 'x36'): 1.952660, ('x8', 'x37'): 2.052481, ('x8', 'x38'): 1.978808, ('x8', 'x39'): 1.985647, ('x8', 'x40'): 2.104199, ('x8', 'x41'): 2.086359, ('x8', 'x42'): 2.238100, ('x8', 'x43'): 2.184059, ('x8', 'x44'): 1.910088, ('x8', 'x45'): 2.064119, ('x8', 'x46'): 2.248596, ('x8', 'x47'): 2.257628, ('x8', 'x48'): 2.208792, ('x8', 'x49'): 1.986817, ('x9', 'x10'): 1.625383, ('x9', 'x11'): 1.786785, ('x9', 'x12'): 1.931865, ('x9', 'x13'): 2.052402, ('x9', 'x14'): 1.865778, ('x9', 'x15'): 1.745411, ('x9', 'x16'): 1.973309, ('x9', 'x17'): 2.021693, ('x9', 'x18'): 1.862032, ('x9', 'x19'): 1.425872, ('x9', 'x20'): 1.864169, ('x9', 'x21'): 1.902406, ('x9', 'x22'): 1.972362, ('x9', 'x23'): 1.572502, ('x9', 'x24'): 1.894099, ('x9', 'x25'): 1.802785, ('x9', 'x26'): 2.352517, ('x9', 'x27'): 1.843872, ('x9', 'x28'): 1.782215, ('x9', 'x29'): 2.274429, ('x9', 'x30'): 1.810061, ('x9', 'x31'): 1.896403, ('x9', 'x32'): 1.961687, ('x9', 'x33'): 2.229506, ('x9', 'x34'): 1.639054, ('x9', 'x35'): 2.315862, ('x9', 'x36'): 2.107770, ('x9', 'x37'): 1.880527, ('x9', 'x38'): 2.048244, ('x9', 'x39'): 2.032674, ('x9', 'x40'): 1.762790, ('x9', 'x41'): 1.803403, ('x9', 'x42'): 1.457963, ('x9', 'x43'): 1.580988, ('x9', 'x44'): 2.204686, ('x9', 'x45'): 1.854032, ('x9', 'x46'): 1.434069, ('x9', 'x47'): 1.413509, ('x9', 'x48'): 1.524684, ('x9', 'x49'): 2.030012, ('x10', 'x11'): 2.232211, ('x10', 'x12'): 2.074205, ('x10', 'x13'): 1.942930, ('x10', 'x14'): 2.146180, ('x10', 'x15'): 2.277271, ('x10', 'x16'): 2.029069, ('x10', 'x17'): 1.976374, ('x10', 'x18'): 2.150260, ('x10', 'x19'): 2.625278, ('x10', 'x20'): 2.147932, ('x10', 'x21'): 2.106289, ('x10', 'x22'): 2.030100, ('x10', 'x23'): 2.465585, ('x10', 'x24'): 2.115336, ('x10', 'x25'): 2.214785, ('x10', 'x26'): 1.616077, ('x10', 'x27'): 2.170038, ('x10', 'x28'): 2.237188, ('x10', 'x29'): 1.701121, ('x10', 'x30'): 2.206861, ('x10', 'x31'): 2.112827, ('x10', 'x32'): 2.041726, ('x10', 'x33'): 1.750046, ('x10', 'x34'): 2.393103, ('x10', 'x35'): 1.655997, ('x10', 'x36'): 1.882629, ('x10', 'x37'): 2.130117, ('x10', 'x38'): 1.947457, ('x10', 'x39'): 1.964415, ('x10', 'x40'): 2.258343, ('x10', 'x41'): 2.214113, ('x10', 'x42'): 2.590328, ('x10', 'x43'): 2.456342, ('x10', 'x44'): 1.777079, ('x10', 'x45'): 2.158972, ('x10', 'x46'): 2.616351, ('x10', 'x47'): 2.638743, ('x10', 'x48'): 2.517663, ('x10', 'x49'): 1.967315, ('x11', 'x12'): 2.042234, ('x11', 'x13'): 1.967518, ('x11', 'x14'): 2.083199, ('x11', 'x15'): 2.157810, ('x11', 'x16'): 2.016545, ('x11', 'x17'): 1.986553, ('x11', 'x18'): 2.085521, ('x11', 'x19'): 2.355880, ('x11', 'x20'): 2.084196, ('x11', 'x21'): 2.060495, ('x11', 'x22'): 2.017132, ('x11', 'x23'): 2.264990, ('x11', 'x24'): 2.065644, ('x11', 'x25'): 2.122246, ('x11', 'x26'): 1.781489, ('x11', 'x27'): 2.096778, ('x11', 'x28'): 2.134997, ('x11', 'x29'): 1.829892, ('x11', 'x30'): 2.117736, ('x11', 'x31'): 2.064216, ('x11', 'x32'): 2.023749, ('x11', 'x33'): 1.857738, ('x11', 'x34'): 2.223736, ('x11', 'x35'): 1.804209, ('x11', 'x36'): 1.933198, ('x11', 'x37'): 2.074057, ('x11', 'x38'): 1.970095, ('x11', 'x39'): 1.979747, ('x11', 'x40'): 2.147037, ('x11', 'x41'): 2.121863, ('x11', 'x42'): 2.335988, ('x11', 'x43'): 2.259729, ('x11', 'x44'): 1.873123, ('x11', 'x45'): 2.090480, ('x11', 'x46'): 2.350799, ('x11', 'x47'): 2.363543, ('x11', 'x48'): 2.294630, ('x11', 'x49'): 1.981397, ('x12', 'x13'): 1.989620, ('x12', 'x14'): 2.026587, ('x12', 'x15'): 2.050430, ('x12', 'x16'): 2.005287, ('x12', 'x17'): 1.995703, ('x12', 'x18'): 2.027329, ('x12', 'x19'): 2.113725, ('x12', 'x20'): 2.026906, ('x12', 'x21'): 2.019332, ('x12', 'x22'): 2.005475, ('x12', 'x23'): 2.084680, ('x12', 'x24'): 2.020977, ('x12', 'x25'): 2.039065, ('x12', 'x26'): 1.930173, ('x12', 'x27'): 2.030926, ('x12', 'x28'): 2.043139, ('x12', 'x29'): 1.945640, ('x12', 'x30'): 2.037624, ('x12', 'x31'): 2.020521, ('x12', 'x32'): 2.007589, ('x12', 'x33'): 1.954539, ('x12', 'x34'): 2.071497, ('x12', 'x35'): 1.937433, ('x12', 'x36'): 1.978653, ('x12', 'x37'): 2.023666, ('x12', 'x38'): 1.990444, ('x12', 'x39'): 1.993528, ('x12', 'x40'): 2.046987, ('x12', 'x41'): 2.038943, ('x12', 'x42'): 2.107368, ('x12', 'x43'): 2.082999, ('x12', 'x44'): 1.959455, ('x12', 'x45'): 2.028914, ('x12', 'x46'): 2.112101, ('x12', 'x47'): 2.116174, ('x12', 'x48'): 2.094152, ('x12', 'x49'): 1.994055, ('x13', 'x14'): 1.979552, ('x13', 'x15'): 1.961215, ('x13', 'x16'): 1.995934, ('x13', 'x17'): 2.003305, ('x13', 'x18'): 1.978982, ('x13', 'x19'): 1.912536, ('x13', 'x20'): 1.979307, ('x13', 'x21'): 1.985132, ('x13', 'x22'): 1.995790, ('x13', 'x23'): 1.934874, ('x13', 'x24'): 1.983867, ('x13', 'x25'): 1.969956, ('x13', 'x26'): 2.053703, ('x13', 'x27'): 1.976215, ('x13', 'x28'): 1.966822, ('x13', 'x29'): 2.041807, ('x13', 'x30'): 1.971064, ('x13', 'x31'): 1.984218, ('x13', 'x32'): 1.994163, ('x13', 'x33'): 2.034964, ('x13', 'x34'): 1.945013, ('x13', 'x35'): 2.048119, ('x13', 'x36'): 2.016418, ('x13', 'x37'): 1.981799, ('x13', 'x38'): 2.007350, ('x13', 'x39'): 2.004978, ('x13', 'x40'): 1.963863, ('x13', 'x41'): 1.970050, ('x13', 'x42'): 1.917425, ('x13', 'x43'): 1.936167, ('x13', 'x44'): 2.031182, ('x13', 'x45'): 1.977763, ('x13', 'x46'): 1.913784, ('x13', 'x47'): 1.910652, ('x13', 'x48'): 1.927589, ('x13', 'x49'): 2.004572, ('x14', 'x15'): 2.099343, ('x14', 'x16'): 2.010415, ('x14', 'x17'): 1.991535, ('x14', 'x18'): 2.053837, ('x14', 'x19'): 2.224031, ('x14', 'x20'): 2.053003, ('x14', 'x21'): 2.038082, ('x14', 'x22'): 2.010785, ('x14', 'x23'): 2.166814, ('x14', 'x24'): 2.041324, ('x14', 'x25'): 2.076955, ('x14', 'x26'): 1.862444, ('x14', 'x27'): 2.060923, ('x14', 'x28'): 2.084982, ('x14', 'x29'): 1.892915, ('x14', 'x30'): 2.074116, ('x14', 'x31'): 2.040425, ('x14', 'x32'): 2.014950, ('x14', 'x33'): 1.910444, ('x14', 'x34'): 2.140845, ('x14', 'x35'): 1.876747, ('x14', 'x36'): 1.957947, ('x14', 'x37'): 2.046620, ('x14', 'x38'): 1.981174, ('x14', 'x39'): 1.987250, ('x14', 'x40'): 2.092562, ('x14', 'x41'): 2.076714, ('x14', 'x42'): 2.211509, ('x14', 'x43'): 2.163503, ('x14', 'x44'): 1.920129, ('x14', 'x45'): 2.056958, ('x14', 'x46'): 2.220832, ('x14', 'x47'): 2.228855, ('x14', 'x48'): 2.185473, ('x14', 'x49'): 1.988289, ('x15', 'x16'): 2.019755, ('x15', 'x17'): 1.983944, ('x15', 'x18'): 2.102116, ('x15', 'x19'): 2.424938, ('x15', 'x20'): 2.100534, ('x15', 'x21'): 2.072234, ('x15', 'x22'): 2.020456, ('x15', 'x23'): 2.316410, ('x15', 'x24'): 2.078382, ('x15', 'x25'): 2.145968, ('x15', 'x26'): 1.739087, ('x15', 'x27'): 2.115558, ('x15', 'x28'): 2.161192, ('x15', 'x29'): 1.796883, ('x15', 'x30'): 2.140582, ('x15', 'x31'): 2.076677, ('x15', 'x32'): 2.028357, ('x15', 'x33'): 1.830132, ('x15', 'x34'): 2.267152, ('x15', 'x35'): 1.766216, ('x15', 'x36'): 1.920235, ('x15', 'x37'): 2.088427, ('x15', 'x38'): 1.964292, ('x15', 'x39'): 1.975817, ('x15', 'x40'): 2.175570, ('x15', 'x41'): 2.145510, ('x15', 'x42'): 2.401186, ('x15', 'x43'): 2.310129, ('x15', 'x44'): 1.848503, ('x15', 'x45'): 2.108037, ('x15', 'x46'): 2.418871, ('x15', 'x47'): 2.434088, ('x15', 'x48'): 2.351803, ('x15', 'x49'): 1.977787, ('x16', 'x17'): 1.998317, ('x16', 'x18'): 2.010706, ('x16', 'x19'): 2.044551, ('x16', 'x20'): 2.010540, ('x16', 'x21'): 2.007573, ('x16', 'x22'): 2.002145, ('x16', 'x23'): 2.033173, ('x16', 'x24'): 2.008218, ('x16', 'x25'): 2.015303, ('x16', 'x26'): 1.972646, ('x16', 'x27'): 2.012115, ('x16', 'x28'): 2.016899, ('x16', 'x29'): 1.978705, ('x16', 'x30'): 2.014739, ('x16', 'x31'): 2.008039, ('x16', 'x32'): 2.002973, ('x16', 'x33'): 1.982191, ('x16', 'x34'): 2.028008, ('x16', 'x35'): 1.975490, ('x16', 'x36'): 1.991637, ('x16', 'x37'): 2.009271, ('x16', 'x38'): 1.996256, ('x16', 'x39'): 1.997465, ('x16', 'x40'): 2.018407, ('x16', 'x41'): 2.015255, ('x16', 'x42'): 2.042060, ('x16', 'x43'): 2.032514, ('x16', 'x44'): 1.984117, ('x16', 'x45'): 2.011327, ('x16', 'x46'): 2.043914, ('x16', 'x47'): 2.045510, ('x16', 'x48'): 2.036883, ('x16', 'x49'): 1.997671, ('x17', 'x18'): 1.991299, ('x17', 'x19'): 1.963791, ('x17', 'x20'): 1.991433, ('x17', 'x21'): 1.993845, ('x17', 'x22'): 1.998257, ('x17', 'x23'): 1.973039, ('x17', 'x24'): 1.993321, ('x17', 'x25'): 1.987562, ('x17', 'x26'): 2.022232, ('x17', 'x27'): 1.990153, ('x17', 'x28'): 1.986265, ('x17', 'x29'): 2.017308, ('x17', 'x30'): 1.988021, ('x17', 'x31'): 1.993466, ('x17', 'x32'): 1.997584, ('x17', 'x33'): 2.014474, ('x17', 'x34'): 1.977236, ('x17', 'x35'): 2.019921, ('x17', 'x36'): 2.006797, ('x17', 'x37'): 1.992465, ('x17', 'x38'): 2.003043, ('x17', 'x39'): 2.002061, ('x17', 'x40'): 1.985040, ('x17', 'x41'): 1.987601, ('x17', 'x42'): 1.965815, ('x17', 'x43'): 1.973574, ('x17', 'x44'): 2.012909, ('x17', 'x45'): 1.990794, ('x17', 'x46'): 1.964308, ('x17', 'x47'): 1.963011, ('x17', 'x48'): 1.970023, ('x17', 'x49'): 2.001893, ('x18', 'x19'): 2.230285, ('x18', 'x20'): 2.054482, ('x18', 'x21'): 2.039145, ('x18', 'x22'): 2.011086, ('x18', 'x23'): 2.171471, ('x18', 'x24'): 2.042477, ('x18', 'x25'): 2.079104, ('x18', 'x26'): 1.858604, ('x18', 'x27'): 2.062624, ('x18', 'x28'): 2.087354, ('x18', 'x29'): 1.889926, ('x18', 'x30'): 2.076185, ('x18', 'x31'): 2.041553, ('x18', 'x32'): 2.015367, ('x18', 'x33'): 1.907944, ('x18', 'x34'): 2.144777, ('x18', 'x35'): 1.873307, ('x18', 'x36'): 1.956773, ('x18', 'x37'): 2.047921, ('x18', 'x38'): 1.980649, ('x18', 'x39'): 1.986894, ('x18', 'x40'): 2.095146, ('x18', 'x41'): 2.078856, ('x18', 'x42'): 2.217413, ('x18', 'x43'): 2.168067, ('x18', 'x44'): 1.917900, ('x18', 'x45'): 2.058548, ('x18', 'x46'): 2.226997, ('x18', 'x47'): 2.235244, ('x18', 'x48'): 2.190651, ('x18', 'x49'): 1.987962, ('x19', 'x20'): 2.226717, ('x19', 'x21'): 2.162896, ('x19', 'x22'): 2.046131, ('x19', 'x23'): 2.713543, ('x19', 'x24'): 2.176761, ('x19', 'x25'): 2.329174, ('x19', 'x26'): 1.411610, ('x19', 'x27'): 2.260596, ('x19', 'x28'): 2.363508, ('x19', 'x29'): 1.541946, ('x19', 'x30'): 2.317029, ('x19', 'x31'): 2.172915, ('x19', 'x32'): 2.063948, ('x19', 'x33'): 1.616928, ('x19', 'x34'): 2.602459, ('x19', 'x35'): 1.472790, ('x19', 'x36'): 1.820120, ('x19', 'x37'): 2.199414, ('x19', 'x38'): 1.919474, ('x19', 'x39'): 1.945464, ('x19', 'x40'): 2.395930, ('x19', 'x41'): 2.328143, ('x19', 'x42'): 2.904721, ('x19', 'x43'): 2.699378, ('x19', 'x44'): 1.658356, ('x19', 'x45'): 2.243637, ('x19', 'x46'): 2.944603, ('x19', 'x47'): 2.978920, ('x19', 'x48'): 2.793357, ('x19', 'x49'): 1.949907, ('x20', 'x21'): 2.038539, ('x20', 'x22'): 2.010914, ('x20', 'x23'): 2.168814, ('x20', 'x24'): 2.041819, ('x20', 'x25'): 2.077878, ('x20', 'x26'): 1.860795, ('x20', 'x27'): 2.061653, ('x20', 'x28'): 2.086001, ('x20', 'x29'): 1.891631, ('x20', 'x30'): 2.075005, ('x20', 'x31'): 2.040909, ('x20', 'x32'): 2.015129, ('x20', 'x33'): 1.909370, ('x20', 'x34'): 2.142534, ('x20', 'x35'): 1.875270, ('x20', 'x36'): 1.957443, ('x20', 'x37'): 2.047179, ('x20', 'x38'): 1.980949, ('x20', 'x39'): 1.987097, ('x20', 'x40'): 2.093672, ('x20', 'x41'): 2.077634, ('x20', 'x42'): 2.214044, ('x20', 'x43'): 2.165463, ('x20', 'x44'): 1.919172, ('x20', 'x45'): 2.057641, ('x20', 'x46'): 2.223480, ('x20', 'x47'): 2.231599, ('x20', 'x48'): 2.187697, ('x20', 'x49'): 1.988149, ('x21', 'x22'): 2.007842, ('x21', 'x23'): 2.121293, ('x21', 'x24'): 2.030047, ('x21', 'x25'): 2.055955, ('x21', 'x26'): 1.899981, ('x21', 'x27'): 2.044298, ('x21', 'x28'): 2.061792, ('x21', 'x29'): 1.922137, ('x21', 'x30'): 2.053891, ('x21', 'x31'): 2.029393, ('x21', 'x32'): 2.010870, ('x21', 'x33'): 1.934883, ('x21', 'x34'): 2.102410, ('x21', 'x35'): 1.910381, ('x21', 'x36'): 1.969423, ('x21', 'x37'): 2.033898, ('x21', 'x38'): 1.986312, ('x21', 'x39'): 1.990730, ('x21', 'x40'): 2.067303, ('x21', 'x41'): 2.055780, ('x21', 'x42'): 2.153791, ('x21', 'x43'): 2.118885, ('x21', 'x44'): 1.941925, ('x21', 'x45'): 2.041415, ('x21', 'x46'): 2.160571, ('x21', 'x47'): 2.166404, ('x21', 'x48'): 2.134860, ('x21', 'x49'): 1.991485, ('x22', 'x23'): 2.034349, ('x22', 'x24'): 2.008509, ('x22', 'x25'): 2.015846, ('x22', 'x26'): 1.971675, ('x22', 'x27'): 2.012545, ('x22', 'x28'): 2.017499, ('x22', 'x29'): 1.977950, ('x22', 'x30'): 2.015261, ('x22', 'x31'): 2.008324, ('x22', 'x32'): 2.003078, ('x22', 'x33'): 1.981559, ('x22', 'x34'): 2.029002, ('x22', 'x35'): 1.974621, ('x22', 'x36'): 1.991341, ('x22', 'x37'): 2.009600, ('x22', 'x38'): 1.996124, ('x22', 'x39'): 1.997375, ('x22', 'x40'): 2.019060, ('x22', 'x41'): 2.015796, ('x22', 'x42'): 2.043552, ('x22', 'x43'): 2.033667, ('x22', 'x44'): 1.983554, ('x22', 'x45'): 2.011728, ('x22', 'x46'): 2.045472, ('x22', 'x47'): 2.047124, ('x22', 'x48'): 2.038191, ('x22', 'x49'): 1.997589, ('x23', 'x24'): 2.131617, ('x23', 'x25'): 2.245105, ('x23', 'x26'): 1.561882, ('x23', 'x27'): 2.194041, ('x23', 'x28'): 2.270669, ('x23', 'x29'): 1.658931, ('x23', 'x30'): 2.236061, ('x23', 'x31'): 2.128753, ('x23', 'x32'): 2.047616, ('x23', 'x33'): 1.714763, ('x23', 'x34'): 2.448594, ('x23', 'x35'): 1.607438, ('x23', 'x36'): 1.866061, ('x23', 'x37'): 2.148484, ('x23', 'x38'): 1.940040, ('x23', 'x39'): 1.959392, ('x23', 'x40'): 2.294811, ('x23', 'x41'): 2.244337, ('x23', 'x42'): 2.673659, ('x23', 'x43'): 2.520760, ('x23', 'x44'): 1.745611, ('x23', 'x45'): 2.181413, ('x23', 'x46'): 2.703356, ('x23', 'x47'): 2.728908, ('x23', 'x48'): 2.590737, ('x23', 'x49'): 1.962701, ('x24', 'x25'): 2.060718, ('x24', 'x26'): 1.891468, ('x24', 'x27'): 2.048068, ('x24', 'x28'): 2.067051, ('x24', 'x29'): 1.915510, ('x24', 'x30'): 2.058478, ('x24', 'x31'): 2.031895, ('x24', 'x32'): 2.011796, ('x24', 'x33'): 1.929340, ('x24', 'x34'): 2.111127, ('x24', 'x35'): 1.902753, ('x24', 'x36'): 1.966820, ('x24', 'x37'): 2.036783, ('x24', 'x38'): 1.985147, ('x24', 'x39'): 1.989941, ('x24', 'x40'): 2.073031, ('x24', 'x41'): 2.060528, ('x24', 'x42'): 2.166881, ('x24', 'x43'): 2.129004, ('x24', 'x44'): 1.936982, ('x24', 'x45'): 2.044940, ('x24', 'x46'): 2.174237, ('x24', 'x47'): 2.180567, ('x24', 'x48'): 2.146339, ('x24', 'x49'): 1.990760, ('x25', 'x26'): 1.797886, ('x25', 'x27'): 2.089516, ('x25', 'x28'): 2.124866, ('x25', 'x29'): 1.842657, ('x25', 'x30'): 2.108901, ('x25', 'x31'): 2.059397, ('x25', 'x32'): 2.021966, ('x25', 'x33'): 1.868413, ('x25', 'x34'): 2.206947, ('x25', 'x35'): 1.818902, ('x25', 'x36'): 1.938211, ('x25', 'x37'): 2.068499, ('x25', 'x38'): 1.972339, ('x25', 'x39'): 1.981267, ('x25', 'x40'): 2.136004, ('x25', 'x41'): 2.112718, ('x25', 'x42'): 2.310775, ('x25', 'x43'): 2.240239, ('x25', 'x44'): 1.882644, ('x25', 'x45'): 2.083690, ('x25', 'x46'): 2.324475, ('x25', 'x47'): 2.336263, ('x25', 'x48'): 2.272521, ('x25', 'x49'): 1.982793, ('x26', 'x27'): 1.839993, ('x26', 'x28'): 1.776805, ('x26', 'x29'): 2.281246, ('x26', 'x30'): 1.805343, ('x26', 'x31'): 1.893830, ('x26', 'x32'): 1.960736, ('x26', 'x33'): 2.235208, ('x26', 'x34'): 1.630088, ('x26', 'x35'): 2.323708, ('x26', 'x36'): 2.110447, ('x26', 'x37'): 1.877559, ('x26', 'x38'): 2.049443, ('x26', 'x39'): 2.033485, ('x26', 'x40'): 1.756897, ('x26', 'x41'): 1.798519, ('x26', 'x42'): 1.444498, ('x26', 'x43'): 1.570580, ('x26', 'x44'): 2.209770, ('x26', 'x45'): 1.850406, ('x26', 'x46'): 1.420010, ('x26', 'x47'): 1.398940, ('x26', 'x48'): 1.512876, ('x26', 'x49'): 2.030757, ('x27', 'x28'): 2.098852, ('x27', 'x29'): 1.875437, ('x27', 'x30'): 2.086213, ('x27', 'x31'): 2.047022, ('x27', 'x32'): 2.017390, ('x27', 'x33'): 1.895827, ('x27', 'x34'): 2.163833, ('x27', 'x35'): 1.856631, ('x27', 'x36'): 1.951083, ('x27', 'x37'): 2.054229, ('x27', 'x38'): 1.978102, ('x27', 'x39'): 1.985169, ('x27', 'x40'): 2.107669, ('x27', 'x41'): 2.089235, ('x27', 'x42'): 2.246030, ('x27', 'x43'): 2.190189, ('x27', 'x44'): 1.907094, ('x27', 'x45'): 2.066254, ('x27', 'x46'): 2.256875, ('x27', 'x47'): 2.266207, ('x27', 'x48'): 2.215745, ('x27', 'x49'): 1.986378, ('x28', 'x29'): 1.826246, ('x28', 'x30'): 2.120259, ('x28', 'x31'): 2.065592, ('x28', 'x32'): 2.024258, ('x28', 'x33'): 1.854689, ('x28', 'x34'): 2.228532, ('x28', 'x35'): 1.800013, ('x28', 'x36'): 1.931766, ('x28', 'x37'): 2.075644, ('x28', 'x38'): 1.969454, ('x28', 'x39'): 1.979313, ('x28', 'x40'): 2.150189, ('x28', 'x41'): 2.124475, ('x28', 'x42'): 2.343189, ('x28', 'x43'): 2.265296, ('x28', 'x44'): 1.870404, ('x28', 'x45'): 2.092419, ('x28', 'x46'): 2.358318, ('x28', 'x47'): 2.371335, ('x28', 'x48'): 2.300945, ('x28', 'x49'): 1.980998, ('x29', 'x30'): 1.848462, ('x29', 'x31'): 1.917348, ('x29', 'x32'): 1.969433, ('x29', 'x33'): 2.183106, ('x29', 'x34'): 1.712029, ('x29', 'x35'): 2.252003, ('x29', 'x36'): 2.085981, ('x29', 'x37'): 1.904682, ('x29', 'x38'): 2.038491, ('x29', 'x39'): 2.026068, ('x29', 'x40'): 1.810748, ('x29', 'x41'): 1.843150, ('x29', 'x42'): 1.567550, ('x29', 'x43'): 1.665702, ('x29', 'x44'): 2.163303, ('x29', 'x45'): 1.883543, ('x29', 'x46'): 1.548486, ('x29', 'x47'): 1.532083, ('x29', 'x48'): 1.620781, ('x29', 'x49'): 2.023944, ('x30', 'x31'): 2.057205, ('x30', 'x32'): 2.021156, ('x30', 'x33'): 1.873268, ('x30', 'x34'): 2.199311, ('x30', 'x35'): 1.825583, ('x30', 'x36'): 1.940490, ('x30', 'x37'): 2.065972, ('x30', 'x38'): 1.973360, ('x30', 'x39'): 1.981958, ('x30', 'x40'): 2.130986, ('x30', 'x41'): 2.108560, ('x30', 'x42'): 2.299309, ('x30', 'x43'): 2.231375, ('x30', 'x44'): 1.886974, ('x30', 'x45'): 2.080602, ('x30', 'x46'): 2.312503, ('x30', 'x47'): 2.323856, ('x30', 'x48'): 2.262466, ('x30', 'x49'): 1.983428, ('x31', 'x32'): 2.011539, ('x31', 'x33'): 1.930878, ('x31', 'x34'): 2.108709, ('x31', 'x35'): 1.904869, ('x31', 'x36'): 1.967542, ('x31', 'x37'): 2.035983, ('x31', 'x38'): 1.985470, ('x31', 'x39'): 1.990159, ('x31', 'x40'): 2.071443, ('x31', 'x41'): 2.059211, ('x31', 'x42'): 2.163250, ('x31', 'x43'): 2.126197, ('x31', 'x44'): 1.938353, ('x31', 'x45'): 2.043962, ('x31', 'x46'): 2.170446, ('x31', 'x47'): 2.176639, ('x31', 'x48'): 2.143155, ('x31', 'x49'): 1.990961, ('x32', 'x33'): 1.974437, ('x32', 'x34'): 2.040203, ('x32', 'x35'): 1.964818, ('x32', 'x36'): 1.987996, ('x32', 'x37'): 2.013307, ('x32', 'x38'): 1.994626, ('x32', 'x39'): 1.996361, ('x32', 'x40'): 2.026421, ('x32', 'x41'): 2.021898, ('x32', 'x42'): 2.060374, ('x32', 'x43'): 2.046671, ('x32', 'x44'): 1.977202, ('x32', 'x45'): 2.016258, ('x32', 'x46'): 2.063035, ('x32', 'x47'): 2.065325, ('x32', 'x48'): 2.052942, ('x32', 'x49'): 1.996657, ('x33', 'x34'): 1.759168, ('x33', 'x35'): 2.210751, ('x33', 'x36'): 2.071907, ('x33', 'x37'): 1.920285, ('x33', 'x38'): 2.032190, ('x33', 'x39'): 2.021801, ('x33', 'x40'): 1.841728, ('x33', 'x41'): 1.868825, ('x33', 'x42'): 1.638340, ('x33', 'x43'): 1.720425, ('x33', 'x44'): 2.136571, ('x33', 'x45'): 1.902607, ('x33', 'x46'): 1.622397, ('x33', 'x47'): 1.608679, ('x33', 'x48'): 1.682857, ('x33', 'x49'): 2.020024, ('x34', 'x35'): 1.668551, ('x34', 'x36'): 1.886912, ('x34', 'x37'): 2.125369, ('x34', 'x38'): 1.949375, ('x34', 'x39'): 1.965714, ('x34', 'x40'): 2.248915, ('x34', 'x41'): 2.206299, ('x34', 'x42'): 2.568784, ('x34', 'x43'): 2.439688, ('x34', 'x44'): 1.785214, ('x34', 'x45'): 2.153171, ('x34', 'x46'): 2.593858, ('x34', 'x47'): 2.615432, ('x34', 'x48'): 2.498771, ('x34', 'x49'): 1.968508, ('x35', 'x36'): 2.098963, ('x35', 'x37'): 1.890291, ('x35', 'x38'): 2.044302, ('x35', 'x39'): 2.030004, ('x35', 'x40'): 1.782175, ('x35', 'x41'): 1.819469, ('x35', 'x42'): 1.502259, ('x35', 'x43'): 1.615231, ('x35', 'x44'): 2.187958, ('x35', 'x45'): 1.865961, ('x35', 'x46'): 1.480318, ('x35', 'x47'): 1.461438, ('x35', 'x48'): 1.563527, ('x35', 'x49'): 2.027559, ('x36', 'x37'): 1.962568, ('x36', 'x38'): 2.015115, ('x36', 'x39'): 2.010237, ('x36', 'x40'): 1.925680, ('x36', 'x41'): 1.938404, ('x36', 'x42'): 1.830174, ('x36', 'x43'): 1.868719, ('x36', 'x44'): 2.064130, ('x36', 'x45'): 1.954267, ('x36', 'x46'): 1.822688, ('x36', 'x47'): 1.816246, ('x36', 'x48'): 1.851079, ('x36', 'x49'): 2.009403, ('x37', 'x38'): 1.983243, ('x37', 'x39'): 1.988651, ('x37', 'x40'): 2.082391, ('x37', 'x41'): 2.068285, ('x37', 'x42'): 2.188268, ('x37', 'x43'): 2.145537, ('x37', 'x44'): 1.928906, ('x37', 'x45'): 2.050699, ('x37', 'x46'): 2.196567, ('x37', 'x47'): 2.203708, ('x37', 'x48'): 2.165093, ('x37', 'x49'): 1.989576, ('x38', 'x39'): 2.004583, ('x38', 'x40'): 1.966730, ('x38', 'x41'): 1.972426, ('x38', 'x42'): 1.923976, ('x38', 'x43'): 1.941231, ('x38', 'x44'): 2.028709, ('x38', 'x45'): 1.979527, ('x38', 'x46'): 1.920624, ('x38', 'x47'): 1.917740, ('x38', 'x48'): 1.933334, ('x38', 'x49'): 2.004209, ('x39', 'x40'): 1.977468, ('x39', 'x41'): 1.981325, ('x39', 'x42'): 1.948512, ('x39', 'x43'): 1.960198, ('x39', 'x44'): 2.019443, ('x39', 'x45'): 1.986135, ('x39', 'x46'): 1.946242, ('x39', 'x47'): 1.944289, ('x39', 'x48'): 1.954850, ('x39', 'x49'): 2.002851, ('x40', 'x41'): 2.135578, ('x40', 'x42'): 2.373800, ('x40', 'x43'): 2.288959, ('x40', 'x44'): 1.858845, ('x40', 'x45'): 2.100662, ('x40', 'x46'): 2.390278, ('x40', 'x47'): 2.404456, ('x40', 'x48'): 2.327788, ('x40', 'x49'): 1.979303, ('x41', 'x42'): 2.309802, ('x41', 'x43'): 2.239486, ('x41', 'x44'): 1.883012, ('x41', 'x45'): 2.083428, ('x41', 'x46'): 2.323458, ('x41', 'x47'): 2.335209, ('x41', 'x48'): 2.271667, ('x41', 'x49'): 1.982847, ('x42', 'x43'): 2.660286, ('x42', 'x44'): 1.677453, ('x42', 'x45'): 2.230018, ('x42', 'x46'): 2.891804, ('x42', 'x47'): 2.924203, ('x42', 'x48'): 2.749011, ('x42', 'x49'): 1.952707, ('x43', 'x44'): 1.750661, ('x43', 'x45'): 2.177811, ('x43', 'x46'): 2.689393, ('x43', 'x47'): 2.714438, ('x43', 'x48'): 2.579010, ('x43', 'x49'): 1.963441, ('x44', 'x45'): 1.913140, ('x44', 'x46'): 1.663234, ('x44', 'x47'): 1.651000, ('x44', 'x48'): 1.717156, ('x44', 'x49'): 2.017859, ('x45', 'x46'): 2.240158, ('x45', 'x47'): 2.248883, ('x45', 'x48'): 2.201705, ('x45', 'x49'): 1.987264, ('x46', 'x47'): 2.964944, ('x46', 'x48'): 2.782030, ('x46', 'x49'): 1.950623, ('x47', 'x48'): 2.810440, ('x47', 'x49'): 1.948829, ('x48', 'x49'): 1.958529}
Q = dict(linear)
Q.update(quadratic)
response = EmbeddingComposite(DWaveSampler()).sample_qubo(Q, num_reads=1000)
for datum in response.data():
    print(datum)