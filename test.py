
import numpy as np
import math
import time
import random
from matplotlib import pyplot as plt


params = {'x': 6.107114700510619, 'is_reversed': False, 'distance_from_center': 0.11497565484011721, 'all_wheels_on_track': True, 'track_width': 0.5966132129340461, 'steps': 14, 'is_left_of_center': True, 'waypoints': [(2.909995283569139, 0.6831924746239328), (3.3199952311658905, 0.6833390533713652), (3.41999521838461, 0.6833748042853732), (3.6300023417267235, 0.6834498837610459), (4.189995119968753, 0.6836500863232341), (4.500002230529587, 0.6837609167129147), (4.549995073956144, 0.6837787896136626), (5.320002125723089, 0.6840540742077795), (5.420002112941809, 0.6840898251217875), (5.7800020669292005, 0.684218528412216), (6.289747858140073, 0.6921400142174), (6.460906484698166, 0.7123063542781353), (6.5136980596947165, 0.7210294115664316), (6.704287871536597, 0.799598672280553), (6.836281775656231, 0.8817004790362547), (6.991663362669656, 1.0062653214908401), (7.1142074641408275, 1.1693225137564909), (7.165830682349035, 1.263426756737598), (7.280019741788613, 1.7628308313393968), (7.272892208655982, 1.8132370038722583), (7.265960701310593, 1.8622568749360433), (7.1045747673751585, 2.3014874894475916), (7.011749008840918, 2.419260292916218), (6.727273712845888, 2.6474924751765463), (6.536921216759571, 2.7266447610626687), (6.079802178702642, 2.773360773339069), (5.919813651266964, 2.772005974951175), (5.719827991972368, 2.7703124769663074), (5.670000926947205, 2.7698905365406308), (5.200034627604903, 2.765910816276192), (5.049876033335467, 2.7646392587170006), (5.002030872389276, 2.768980714618128), (4.942709994269048, 2.775327848322301), (4.561340171137485, 2.898322513024676), (4.258533108743229, 3.166955220685885), (4.092728535429521, 3.3703748558215287), (4.001121969780925, 3.482763638518189), (3.774000078716213, 3.761411273431655), (3.6823935130676184, 3.8738000561283137), (3.5490587458571623, 4.037383660336441), (3.2758532950668884, 4.333295323360169), (3.1911463583891155, 4.385684825652305), (3.0954945192403103, 4.435922305057415), (2.9549738926202442, 4.484413606024224), (2.8089822299540046, 4.500038654567632), (2.8110045575773057, 4.499832029419236), (2.5003276964136627, 4.498718163592657), (2.249377566090162, 4.491428972830993), (1.990177178741659, 4.483900142037221), (1.7395172672798365, 4.476619381080485), (1.1871156114665855, 4.391792930201858), (1.1054389398706574, 4.3402307341807065), (0.7316196323127645, 3.819658838269335), (0.7080468873794841, 3.5295953182618844), (0.8747319412102282, 2.7251244177375193), (0.8863119620897287, 2.6692358445815714), (0.9180990438541362, 2.5158220758940644), (0.9380374746317692, 2.4195933679559642), (1.0212099341560652, 2.0181787127447155), (1.043063552869095, 1.912706746772055), (1.0936256517149223, 1.6686792454688633), (1.219724413480236, 1.169889412099395), (1.2404620134668318, 1.1182110370035536), (1.286611404297767, 1.0270193376917442), (1.3195344250237366, 0.9895904728963364), (1.3897426105955222, 0.9097735962139227), (1.4563853812178036, 0.8435308547287804), (1.4996428710531535, 0.8193608401945228), (2.0400025449490777, 0.6828814442283201), (2.7500024542019887, 0.6831352757177762), (2.909995283569139, 0.6831924746239328)], 'closest_waypoints': [9, 10], 'y': 0.8042914189309017, 'progress': 3.102106460231577, 'heading': 14.950637902847403, 'steering_angle': -14.999999999999998, 'speed': 0.4}

# Oval Track
#params =  {'heading': -0.8942166156046021, 'is_left_of_center': False, 'waypoints': [(2.973129727863096, 0.9587203451227853), (3.1686550001583385, 0.957973927514008), (3.3641587621388993, 0.957502662680531), (3.5596536099349976, 0.9571676056167091), (3.7551399311198708, 0.9569079073242543), (3.9506256709448877, 0.9566988842326032), (4.146107922610766, 0.9565304352142532), (4.341591530782978, 0.9563990236634121), (4.537073588662238, 0.9563010645276331), (4.732557196834449, 0.9562337963475989), (4.92803925471371, 0.9561973644632735), (5.123521506379589, 0.9561847441097273), (5.3190037580454685, 0.9562067146676283), (5.514486009711348, 0.9562466104877638), (5.709974462549027, 0.9563314648034498), (5.905463109173326, 0.9564632639275283), (6.10095815075604, 0.9566372843111675), (6.296465594682358, 0.956848729735553), (6.491997261936018, 0.9569796325965199), (6.6875785385640825, 0.9567336689306691), (6.883257677434614, 0.9557806263396478), (7.079130990497134, 0.9538671530427651), (7.275221344572657, 0.9543163504250318), (7.4705043835944585, 0.968040367211689), (7.662157411673801, 1.00506531126039), (7.845235769446617, 1.0715002572806311), (8.014446369208315, 1.1684281333446516), (8.165421648145468, 1.2924605804235763), (8.294117279524725, 1.4398041043387009), (8.397584218581926, 1.6056121986483556), (8.469351930116943, 1.7860276860462465), (8.511767170082862, 1.9763842816461406), (8.530750119682551, 2.1709724987464085), (8.535956778555175, 2.3671952090825386), (8.538760870928513, 2.563413656113056), (8.537808603483967, 2.75963888567523), (8.532572489045293, 2.95569387369283), (8.51481039514374, 3.15055503924561), (8.475491090199, 3.341414414227855), (8.407975057079398, 3.5247578720951225), (8.31106120632191, 3.693881267878382), (8.186502531679764, 3.844170542185153), (8.037129092933212, 3.969503006795976), (7.868136309330993, 4.066595722602571), (7.6851610460393545, 4.1345014606124835), (7.494133948738579, 4.175703983918254), (7.299554742716083, 4.195335731117524), (7.103587636930088, 4.201242347257079), (6.907607353654015, 4.201247579495785), (6.711783262392657, 4.199924210676329), (6.516154120469764, 4.199300605337186), (6.3205893157042965, 4.199124065727503), (6.125061330396392, 4.199215533011554), (5.929553692683456, 4.199390716114905), (5.734056325661314, 4.199555822314082), (5.538567872823634, 4.1996779078838955), (5.343080582705667, 4.199756585251109), (5.147595618027125, 4.199802318893134), (4.952113560147865, 4.199816465316303), (4.756630145762273, 4.199800962386803), (4.561147894096393, 4.19975794175744), (4.365664285924183, 4.199686628281739), (4.170183390764635, 4.199580045641426), (3.974701139098755, 4.1994405192759245), (3.779218887432876, 4.199264948599335), (3.5837366357669964, 4.199009925409058), (3.3881109820032407, 4.198595803404785), (3.3881109820032407, 4.198595803404785), (3.1927025630391057, 4.198236329227001), (2.997255774324458, 4.197737328683715), (2.801790188307791, 4.197125156755078), (2.6062952436183835, 4.195692686069265), (2.410804949807826, 4.190964292571721), (2.2150827903079318, 4.183555248776983), (2.0190451461927097, 4.16967140647651), (1.8255455254232797, 4.1381578265350925), (1.6399065197169342, 4.077816355401538), (1.4684209619443997, 3.98580995697732), (1.316564535251782, 3.863567226215878), (1.18828627180266, 3.716441712246848), (1.087181058714844, 3.5495077176822467), (1.0159622477774413, 3.3684589840609287), (0.9734102913519926, 3.178145699770326), (0.9534938958331036, 2.9834065228940503), (0.9444216541596013, 2.7872029974331767), (0.9405074066940884, 2.5907339843046135), (0.9396984929007637, 2.3942255355991335), (0.9471365077950047, 2.1980486557983383), (0.9667406161777752, 2.003330698556816), (1.008643508547042, 1.8129062776403588), (1.0777365771700467, 1.6310002804643384), (1.1746683531897695, 1.460860280079107), (1.2993533282606862, 1.3105290994160301), (1.4485447529255744, 1.1851194108376364), (1.618276541798405, 1.0898755162672418), (1.80267831683733, 1.026955253927975), (1.9950098887622332, 0.9923725057420933), (2.190220548481932, 0.9752908935522877), (2.3860145059240736, 0.9666594679897911), (2.581804490740531, 0.9621571992530031), (2.77751667022956, 0.9599051322865064), (2.973129727863096, 0.9587203451227853)], 'steps': 1, 'y': 0.9564181222148141, 'is_reversed': False, 'distance_from_center': 0.001746928303460121, 'steering_angle': -29.999999999999996, 'x': 3.118586692693628, 'speed': 0.4, 'progress': 0.7440725341828801, 'all_wheels_on_track': True, 'closest_waypoints': [0, 1], 'track_width': 0.6096313811114228}

# Tokyo Track
# params = {'is_left_of_center': False, 'waypoints': [(3.9968843292236325, -2.398085115814209), (4.108486819458006, -2.398085115814209), (4.220117408752442, -2.398085115814209), (4.331728619384766, -2.3980848251342772), (4.443350294494627, -2.398085115814209), (4.554988441467286, -2.398085115814209), (4.666571746826172, -2.398085115814209), (4.7781641601562495, -2.398085115814209), (4.8896753768920895, -2.398085115814209), (5.001236978149414, -2.398085115814209), (5.112820671081545, -2.398085115814209), (5.22445222930908, -2.398085115814209), (5.336061114501954, -2.398085115814209), (5.4476612792968755, -2.3980848251342772), (5.559263769531249, -2.398085115814209), (5.670884088134765, -2.398085115814209), (5.782510801696777, -2.398085115814209), (5.894127050781252, -2.398085115814209), (6.00181679534912, -2.398085115814209), (6.173943692016602, -2.398085115814209), (6.345643870544436, -2.398085115814209), (6.537344378662107, -2.398085115814209), (6.768550421142578, -2.398085115814209), (6.98473063659668, -2.398085115814209), (7.162758142089844, -2.398085115814209), (7.274807891845702, -2.398085115814209), (7.3869537597656265, -2.398085115814209), (7.499844155883789, -2.398085115814209), (7.61068235168457, -2.384343028259277), (7.715040710449218, -2.3489811363220214), (7.806151428222655, -2.289116379547119), (7.879453155517577, -2.2083449531555175), (7.931933673095703, -2.1111327667236326), (7.969687957763672, -2.0054785568237286), (8.009337475585937, -1.9026145835876465), (8.063614782714842, -1.8110042839050309), (8.13654327697754, -1.734422282028198), (8.224194903564452, -1.670004508590698), (8.315116873168945, -1.6062793285369872), (8.397656408691406, -1.5321647148132325), (8.462792355346679, -1.44245458984375), (8.509496481323243, -1.3409916938781739), (8.540622875976563, -1.2328676250457764), (8.560585998535156, -1.12199483833313), (8.572986404418945, -1.010168572998047), (8.580685159301758, -0.8628370136260985), (8.583536148071289, -0.7021988536834717), (8.58443454284668, -0.5753229497909546), (8.584472137451172, -0.3747735631942749), (8.584492291259764, -0.19896346716880797), (8.584528335571289, -0.00428482018969953), (8.584556240844726, 0.2119464259147644), (8.58433532409668, 0.3881836337089538), (8.584120608520507, 0.5002564319610595), (8.580803369140625, 0.6122315738677978), (8.571400067138672, 0.7239659116744994), (8.555663430786133, 0.8350995351791382), (8.531425762939453, 0.9447460159301757), (8.500583847045899, 1.0525313941955565), (8.46601541442871, 1.1590160766601563), (8.431132659912109, 1.2648468261718748), (8.40480791015625, 1.3722508808135987), (8.388611611938476, 1.4806030849456786), (8.405742349243162, 1.6502103195190427), (8.463046215820313, 1.8476967147827148), (8.53134553527832, 2.0626024925231934), (8.55994340209961, 2.291900899505615), (8.514377191162108, 2.4563697364807124), (8.426188388061522, 2.610280400085449), (8.300192977905272, 2.7344502433776854), (8.126715969848632, 2.814492935180664), (7.936248913574218, 2.8448311027526856), (7.69728442993164, 2.842157622528076), (7.414035440063476, 2.8335633796691893), (7.165993991088866, 2.8013261032104495), (6.971922503662109, 2.736647105407715), (6.792461752319335, 2.6331662124633786), (6.649091239929199, 2.4822172866821286), (6.649091239929199, 2.4822172866821286), (6.544510801696777, 2.30300177230835), (6.491997534179687, 2.1105175910949705), (6.481333262634276, 1.915810774230957), (6.498144058227538, 1.7427884864807128), (6.531408113098145, 1.5830480915069578), (6.566860212707519, 1.4499332515716552), (6.603410694885254, 1.3282434410095214), (6.641890516662597, 1.2071183731079103), (6.678002847290038, 1.0942358253479), (6.713907051086426, 0.9754661369323733), (6.748999676513671, 0.8351240734100341), (6.771528340148926, 0.6824846742630002), (6.770214854431152, 0.5170887620925904), (6.739964762878418, 0.35214239854812623), (6.678730709838867, 0.20278325449079276), (6.584536071777343, 0.073577370595932), (6.465435395812988, -0.022756241798400884), (6.332671018981934, -0.08443354539871215), (6.192271061706543, -0.11442267904281617), (6.048808113098144, -0.11327295513153077), (5.9084566024780285, -0.0796875414848329), (5.777142330932618, -0.017066400146484362), (5.654321920776367, 0.04993410081863381), (5.543534690856934, 0.08980346956253056), (5.431823098754883, 0.10004641265869134), (5.321303681945801, 0.08101749906539898), (5.223240675354005, 0.0331226148605349), (5.136034951782227, -0.03443096523284911), (5.057559121704101, -0.11292725191116332), (4.981652514648437, -0.19307756190299985), (4.901582789611815, -0.265934788107872), (4.813124816894531, -0.3229467545032501), (4.716816741943359, -0.3564500641271472), (4.6162901260375975, -0.3593997144155204), (4.51511413116455, -0.3368315144300461), (4.416144396972657, -0.29576415982246396), (4.317549252319336, -0.247266593170166), (4.215311694335938, -0.20396510591506956), (4.107997895812988, -0.18035982437133785), (3.999729116821289, -0.184920810508728), (3.8959674270629883, -0.2160716101646423), (3.800001385498047, -0.27164925882816315), (3.709108677673339, -0.33655119952783036), (3.616933296203613, -0.3951910578489304), (3.518029643249511, -0.4385550443172457), (3.4129790786743164, -0.46291566977500914), (3.3047851013183593, -0.4704929507255554), (3.1941414672851565, -0.4655450453758239), (3.0825288032531737, -0.45816466374397274), (2.9700563079833975, -0.4528322554588317), (2.8574543632507323, -0.4456599219322205), (2.7442044929504394, -0.4349176088809967), (2.6292975532531737, -0.4197862710952759), (2.5105101333618163, -0.40448946981430056), (2.3889220123291004, -0.39316141550540923), (2.26488229675293, -0.38975981838703155), (2.1411589378356934, -0.4009938316822052), (2.020786827850342, -0.4341942760944366), (1.8794536911010733, -0.5233404517173774), (1.7949362239837645, -0.6104808813095093), (1.7206921123504637, -0.7506510318756103), (1.6887726943969725, -0.8770849569320678), (1.6724089160919189, -1.0758010009765624), (1.6601904273986814, -1.2993672481536864), (1.6567321598052978, -1.5105078002929688), (1.6593520095825194, -1.6933875289916993), (1.6648058433532715, -1.8153231094360351), (1.6874392971038819, -1.9510643394470213), (1.7280409854888914, -2.050013919830322), (1.7906410888671873, -2.1427592277526855), (1.870859399795532, -2.223833251953125), (1.9645064453124998, -2.2893214057922364), (2.0718011558532714, -2.3412403297424316), (2.18892162322998, -2.375639586639404), (2.3153282485961912, -2.3939165718078614), (2.429082545471191, -2.398216987609863), (2.542245696258545, -2.3981534255981445), (2.6547331130981444, -2.398104203796387), (2.766569309997559, -2.398085115814209), (2.878082949066162, -2.398085115814209), (2.990368634033203, -2.398085115814209), (3.102650637054443, -2.398085115814209), (3.214940197753906, -2.398085115814209), (3.3272259796142576, -2.398085115814209), (3.438768783569336, -2.398085115814209), (3.5503902648925783, -2.398085115814209), (3.6620016693115236, -2.398085115814209), (3.7736411727905272, -2.3980848251342772), (3.8852564529418943, -2.398085115814209), (3.9968843292236325, -2.398085115814209)], 'closest_waypoints': [1, 2], 'speed': 0.4, 'is_reversed': False, 'track_width': 0.6603288844558911, 'x': 4.138348340782516, 'steps': 1, 'progress': 0.62512711120958, 'steering_angle': -29.999999999999996, 'distance_from_center': 0.00013351107196335477, 'all_wheels_on_track': True, 'heading': -0.03467457202103572, 'y': -2.3982186268861723}

print("waypoints size: {}".format(len(params['waypoints'])))
waypoints = np.array(params['waypoints'])

print(len(waypoints))


def calculate_radian(idx, waypoints):
    currentPoint = waypoints[idx]
    nextPoint = waypoints[(idx + 1) % len(waypoints)]
    radian = math.atan2(nextPoint[1]-currentPoint[1], nextPoint[0] - currentPoint[0])
    # radian = math.atan2(nextPoint['y']-currentPoint['y'], nextPoint['x'] - currentPoint['x'])
    degree = track_direction = math.degrees(radian)
    return radian, degree

def calculate_degree_diff(idx, degrees):
    currentDegree = degrees[idx]
    nextDegree = degrees[(idx + 1) % len(degrees)]
    degree_diff = nextDegree - currentDegree
    if (abs(degree_diff) > 180):
        if (degree_diff > 0):
            degree_diff = degree_diff - 360
        else:
            degree_diff = degree_diff + 360
    return degree_diff

def calculate_optimal_speed(idx, degrees_diffs):
    return 0


radian_degree = np.array([calculate_radian(idx, waypoints) for idx in range(len(waypoints))])


# print(radian_degree.T[1])
degree_diff = np.array([calculate_degree_diff(idx, radian_degree.T[1]) for idx in range(len(radian_degree.T[1]))])


result = np.c_[np.arange(len(degree_diff)),  waypoints, radian_degree, degree_diff]
np.set_printoptions(precision=6)
np.set_printoptions(suppress=True)
np.set_printoptions(threshold=2000)

print(result)
# print(np.c_[np.arange(len(radian), dtype='i4'), result] )


# print(np.c_[])

result = result.T

x = result[1]
y = result[2]
radians = result[3]
degrees = result[4]
degree_diffs = result[5]

# print(degrees)

font = {'family' : 'normal',
        'size'   : 6}


plt.rc('font', **font)

fig, ax = plt.subplots()




# fig2, ax2 = plt.subplots()

# ax2.hist(degree_diffs, color = 'blue', edgecolor = 'black',
#          bins = int(360/1))


# plt.tight_layout()

# plt.interactive(True)

# for i in range(10):
#     plt.scatter(i, 0.1, color="r")
#     plt.show()

#     time.sleep(1)



# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro')

# title = ax.text(4 ,0.85, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},
#                 transform=ax.transAxes, ha="center")

# def init():
#     ax.scatter(x,y)
#     # ax.set_xlim(0, 2*np.pi)
#     # ax.set_ylim(-1, 1)
#     return ln,

# def update(frame):

#     x = random.randrange(2, 8)
#     y = random.randrange(-2,2)
#     xdata.append(x)
#     ydata.append(y)
#     ln.set_data(xdata, ydata)
#     tw = random.randint(1,101)
#     # title.set_text(u"{}".format(tw))
#     ax.set_title(tw)

#     return ln,

# ani = FuncAnimation(fig, update, frames=15,
#                     init_func=init, blit=False, repeat=False, interval=1000)
# plt.show()




# for i, txt in enumerate(x):
#     annot = ax.annotate(i, (x[i], y[i]), textcoords="offset points", xytext=(0,0.1))


#     annot.set_visible(False)


q = ax.quiver(x, y, np.cos(radian), np.sin(radian))

# plt.quiverkey(q, x, y , 7, r'vector2',
#                       labelpos='S', coordinates = 'figure')

plt.show()

