import csv
from newspaper import Article

URLS = [
    'https://www.voaswahili.com/a/uchumi-wa-kernya-wakuwa-kwa-asilimia-5-6-/7619683.html',
    'https://www.voaswahili.com/a/wafanyakazi-tanzania-walalamikia-mafao-ya-wastaafu-na-bima-ya-afya-/7593741.html',
    'https://www.voaswahili.com/a/rais-wa-tanzania-atuma-salamu-za-rambirambi-kufuatia-kifo-cha-rais-wa-iran-/7619601.html',
    'https://www.voaswahili.com/a/aliyekuwa-katibu-mkuu-wa-eac-anatarajiwa-kuhojiwa-na-kamati-ya-sheria-haki-na-hadhi-ya-bunge-la-jumuiya-hiyo/7610133.html',
    'https://www.voaswahili.com/a/serikali-ya-tanzania-yasema-wananchi-walivamia-eneo-la-uwanja-wa-ndege-wa-kimataifa-wa-kilimanjaro-kia-/7618915.html',
    'https://www.voaswahili.com/a/kenya-kuomboleza-vifo-kutokana-na-mafuriko-kwa-kupanda-miti/7602740.html',
    'https://www.voaswahili.com/a/tanzania-watetezi-wa-haki-za-binadamu-wataka-serikali-ibuni-sheria-maalum-ya-ukatili-dhidi-ya-wanawake/7614298.html',
    'https://www.voaswahili.com/a/afrika-mashariki-yaweka-mikakati-kukamilisha-ujenzi-wa-reli-ya-sgr-/7599965.html',
    'https://www.voaswahili.com/a/ofisi-ya-rais-afrika-kusini-yapokea-vyema-tangazo-la-mwendesha-mashtaka-wa-mahakama-ya-kimataifa-ya-uhalifu--icc/7620524.html',
    'https://www.voaswahili.com/a/7620522.html',
    'https://www.voaswahili.com/a/rais-wa-mauritania-anakabiliwa-na-upinzani-kwenye-uchaguzi-wa-urais/7620461.html',
    'https://www.voaswahili.com/a/wanajeshi-wa-marekani-walioamriwa-kuondoka-niger-watakamilisha-kuondoka-kwao-katikati-ya-septemba/7618986.html',
    'https://www.voaswahili.com/a/mamia-waandamana-tunis-kumuunga-mkono-rais-kais-saied/7618967.html',
    'https://www.voaswahili.com/a/mamia-waandamana-tunis-kumuunga-mkono-rais-kais-saied/7618967.html',
    'https://www.voaswahili.com/a/jacob-zuma-aahidi-kujenga-viwanda-na-kutoa-elimu-ya-bure-kwa-vijana-wa-afrika-kusini/7618943.html',
    'https://www.voaswahili.com/a/rais-wa-tunisia-anakosoa-uingiliaji-kati-wa-mataifa-ya-kigeni-nchini-mwake/7615838.html',
    'https://www.voaswahili.com/a/7615834.html',
    'https://www.voaswahili.com/a/drone-tano-zilipiga-mkoa-wa-kharkiv-huko-ukraine-na-kusababisha-moto/7615827.html',
    'https://www.voaswahili.com/a/utawala-wa-biden-unaunda-mchakato-mpya-wa-mahakama-za-uhamiaji/7615825.html',
    'https://www.voaswahili.com/a/afrika-kusini-imetoa-wito-kwa-un-kwamba-israel-isitishe-mapigano-gaza/7615823.html',
    'https://www.voaswahili.com/a/yoav-gallant-anasema-wanajeshi-wa-ziada-wa-israel-wataingia-mji-wa-rafah/7615807.html',
    'https://www.voaswahili.com/a/benin-itaruhusu-usafirishaji-mafuta-ya-niger-kupitia-bandari-yake-ya-seme/7614301.html',
    'https://www.voaswahili.com/a/blinken-ametangaza-dola-bilioni-2-za-kufadhili-juhudi-za-kijeshi-za-ukraine/7614299.html',
    'https://www.voaswahili.com/a/white-house-inafanya-juhudi-kuwaondoa-madaktari-waliokwama-gaza/7614282.html',
    'https://www.voaswahili.com/a/yoav-gallant-amemshambulia-netanyahu-kushindwa-kubuni-mpango-kwa-gaza/7614279.html',
    'https://www.voaswahili.com/a/rasoulof-anaiomba-jumuia-ya-filamu-iwalinde-watengeneza-filamu-wenzake/7611635.html',
    'https://www.voaswahili.com/a/marekani-imeweka-vikwazo-kwa-raia-wa-russia-na-makampuni-kutoka-russia/7611633.html',
    'https://www.voaswahili.com/a/7611624.html',
    'https://www.voaswahili.com/a/mahakama-ya-rufaa-nigeria-imempatia-mubarak-bala-kifungo-cha-miaka-mitano/7611622.html',
    'https://www.voaswahili.com/a/katibu-mkuu-wa-un-anasikitishwa-na-harakati-za-kijeshi-zinazoendelea-rafah/7611618.html',
    'https://www.voaswahili.com/a/antony-blinken-ameiahidi-kyiv-msaada-usio-na-masharti-wa-marekani/7611613.html',
    'https://www.voaswahili.com/a/idadi-ya-watu-waliopoteza-makazi-kutokana-na-mizozo-na-ghasia-yavunja-rekodi-duniani-/7610860.html',
    'https://www.voaswahili.com/a/rais-ramaphosa-akanusha-njama-za-kisiasa-kusababisha-kukatika-kwa-huduma-za-umeme-/7610740.html',
    'https://www.voaswahili.com/a/aliyekuwa-katibu-mkuu-wa-eac-anatarajiwa-kuhojiwa-na-kamati-ya-sheria-haki-na-hadhi-ya-bunge-la-jumuiya-hiyo/7610133.html',
    'https://www.voaswahili.com/a/biden-ametoa-amri-ya-kuzuia-kampuni-ya-madini-kumiliki-ardhi-huko-wyoming/7610130.html',
    'https://www.voaswahili.com/a/eu-imeelezea-wasiwasi-kuhusu-vurugu-za-baada-ya-uchaguzi-wa-chad/7610126.html',
    'https://www.voaswahili.com/a/marekani-na-pakistan-zimehitimisha-mazungumzo-ya-kupambana-na-ugaidi/7610125.html',
    'https://www.voaswahili.com/a/watu-watatu-wamefikishwa-mahakama-ya-london-kwa-kusaidia-ujasusi/7610123.html',
    'https://www.voaswahili.com/a/misaada-ya-kibinadamu-inapungua-gaza-anasema-naibu-msemaji-wa-un/7610118.html',
    'https://www.voaswahili.com/a/michael-cohen-ameeleza-kilichojiri-2016-kuhusu-malipo-ya-siri-kwa-stormy-daniels/7610105.html',
    'https://www.voaswahili.com/a/rwanda-yapuuzilia-mbali-madai-ya-burundi-kwamba-iliwapa-silaha-kundi-la-waasi-/7608604.html',
    'https://www.voaswahili.com/a/idadi-ya-vifo-imeongezeka-kufuatia-kuanguka-kwa-jengo-huko-afrika-kusini/7608587.html',
    'https://www.voaswahili.com/a/mashambulizi-ya-kushtukiza-ya-russia-yamewakimbiza-watu-4-000-huko-ukraine/7608586.html',
    'https://www.voaswahili.com/a/ndege-za-kivita-zikiwa-hewani-huku-moja-ikiwa-na-rubani-na-nyingine-haina/7608583.html',
    'https://www.voaswahili.com/a/kampuni-za-china-zimeshinda-zabuni-za-kuchunguza-mafuta-nchini-iraq/7608581.html',
    'https://www.voaswahili.com/a/idadi-ya-vifo-imeongezeka-kutokana-na-mafuriko-nchini-afghanistan/7608578.html',
    'https://www.voaswahili.com/a/michael-cohen-anatarajiwa-kutoa-ushahidi-jumatatu-dhidi-ya-donald-trump/7608572.html',
    'https://www.voaswahili.com/a/tume-ya-uchaguzi-chad-yasema-mahamat-idriss-deby-alishinda-uchaguzi-wa-rais/7605590.html',
    'https://www.voaswahili.com/a/raia-nane-wafariki-dunia-katika-shambulio-dhidi-ya-kituo-kimoja-cha-afya-mashariki-mwa-drc/7605584.html',
    'https://www.voaswahili.com/a/viongozi-wa-afrika-waweka-mkakati-wa-kuboresha-uzalishaji-wa-mbolea-/7604712.html',
    'https://www.voaswahili.com/a/unrwa-inasema-wakimbizi-80-000-wameukimbia-mji-wa-rafah-huko-gaza/7604800.html',
    'https://www.voaswahili.com/a/stormy-daniels-anaendelea-kutoa-ushahidi-wake-dhidi-ya-trump/7604794.html',
    'https://www.voaswahili.com/a/7604714.html',
    'https://www.voaswahili.com/a/maafisa-wa-pakistan-wanalaumu-mauaji-ya-vinyozi-katika-jimbo-la-punjab/7604705.html',
    'https://www.voaswahili.com/a/rais-cyril-ramaphosa-aita-uhaini-tangazo-la-kampeni-ya-chama-cha-upinzani/7604025.html'
]

with open('voa_articles.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['Title', 'Content'])

    for url in URLS:
        article = Article(url)
        article.download()
        article.parse()
        writer.writerow([article.title, article.text])

print('Articles have been saved to articles.csv')
