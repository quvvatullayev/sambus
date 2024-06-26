data_busstp = {
    "hazora bekati":"39.681751, 66.900877" ,
    "texnikum":"39.677556, 66.910170",
    "seleno":"39.674152, 66.916687",
    "pedinstitut":"39.670868, 66.921353",
    "pavarod":"39.664661, 66.929674",
    "zafar rastok":"39.662884, 66.933482",
    "selhoz":"39.662007, 66.935205",
    "bog'shamol":"39.660744, 66.937792",
    "oblasnoy kasal xona":"39.658943, 66.943759",
    "dinamo":"39.657824, 66.947343",
    "over":"39.656316, 66.950628",
    "go'm":"39.655764, 66.957090",
    "viloyat hokimyat":"39.655195, 66.961609",
    "iniyaz":"39.651979, 66.962278",
    "bulvar":"39.649385, 66.964595",
    "aroq zavod":"39.653102, 66.972717",
    "registon":"39.653509, 66.978683",
    "27 maktab":"39.650063, 66.983442",
    "ko'ptarmoqli raddom":"39.647705, 66.989991",
    "avashnoy":"39.646224, 66.996844",
    "5 paliklinika":"39.656261, 67.000904",
    "trikatajka":"39.660054, 67.002398",
    "65 maktab":"39.659535, 67.008235",
    "kavhoz":"39.658625, 67.019481",
    "papeda":"39.657511, 67.026984",
    "samarqand city":"39.655973, 67.051216",
    "trikatajka":"39.660631, 67.001573",
    "gagarin":"39.661848, 66.997766",
    "yangi bozor":"39.662926, 66.994386",
    "shohi zinda":"39.662444, 66.989898",
    "siyob bozor":"39.665193, 66.980143",
    "xavasiy":"39.667194, 66.974576",
    "dagbetiskey":"39.668669, 66.969369",
    "tibbiyot texnikum":"39.669299, 66.967931",
    "kirpijka":"39.673260, 66.955989",
    "6 hammom":"39.675742, 66.949305",
    "gar zaparavka":"39.677235, 66.943614",
    "oltin samarqand":"39.679294, 66.939242",
    "elita bekati":"39.681122, 66.934629",
    "vakzal bozor":"39.682098, 66.929771",
    'vakzal':"39.681581, 66.928421",
    "parik yoshlik":"39.679082, 66.927437",
    "eski beelny":"39.675043, 66.926046",
    "opshita":"39.678390, 66.921018",
    "tramma talogiya":"39.679670, 66.919125",
    "obil gayiy":"39.675808, 66.914682",
    "sag":"39.679267, 66.907208",
    "choy xonat":"39.679992, 66.904937",
    "danlaget bozor":"39.685591, 66.895849",
    "do'stlik":"39.690731, 66.881706",
 }

import requests

url = 'http://findbus.pythonanywhere.com/bus_ip/busstop/'

for basstop in data_busstp.items():
    busstop_name = basstop[0]
    latitude = basstop[-1].split(', ')[0]
    longitude = basstop[-1].split(', ')[-1]

    data = {
      "busstop_name": busstop_name,
      "latitude": latitude,
      "longitude": longitude,
    }

    req = requests.post(url=url, data=data)
    print(req.status_code, req.json())