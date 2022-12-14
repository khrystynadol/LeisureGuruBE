from models import app, db, Place, Season, Activity, PlaceActivity, PlaceSeason, User, PlacePhoto
from werkzeug.security import generate_password_hash

with app.app_context():
    user_1 = User(first_name="Mary", last_name="Smith", birth_date="2002-10-22",
                  email="user1@gmail.com", password=generate_password_hash("12345"),
                  photo="https://i.pinimg.com/564x/41/ce/13/41ce1334108664fced76d7e7095ee8a7.jpg",
                  verification=True)

    user_2 = User(first_name="John", last_name="Anderson", birth_date="2000-01-12",
                  email="user2@gmail.com", password=generate_password_hash("12345"),
                  photo="https://i.pinimg.com/564x/bd/63/b1/bd63b14ac4a068e0971e5490ba884036.jpg",
                  verification=True)

    season1 = Season(name="winter")
    season2 = Season(name="spring")
    season3 = Season(name="summer")
    season4 = Season(name="autumn")

    activity1 = Activity(name="Sightseeing")
    activity2 = Activity(name="Hiking")
    activity3 = Activity(name="Mountain biking")
    activity4 = Activity(name="Rowing")
    activity5 = Activity(name="Cycling")
    activity6 = Activity(name="Swimming")
    activity7 = Activity(name="Eating out")
    # activity8 = Activity(name="Rafting")
    db.session.add_all([season1, season2, season3, season4,
                        activity1, activity2, activity3, activity4, activity5,
                        activity6, activity7,
                        user_1, user_2])
    db.session.commit()

    place1 = Place(name="Lviv Theatre of Opera and Ballet", country="Ukraine", city="Lviv",
                   description="Lviv’s resplendent opera house is one of the city’s symbols and stands alone on "
                               "Freedom Square. A design competition in the 1890s was won by Polish architect Zygmunt "
                               "Gorgolewski, and he made a few technical innovations: This location had been "
                               "marshland, watered by the Poltva River, which was diverted underground. The theatre "
                               "was then built onto a concrete platform, and after sinking for a couple of years "
                               "eventually stabilised. Almost 120 years later, this marvellous venue remains the "
                               "place to get a blast of high culture at a matinee or evening performance, where "
                               "seats are implausibly inexpensive. In residence is a 90-piece orchestra, first-class "
                               "soloists and a ballet troupe, all with an extensive repertoire.",
                   rate=5,
                   image="https://cdn.thecrazytourist.com/wp-content/"
                         "uploads/2018/08/ccimage-shutterstock_212603344.jpg",
                   visible=True)
    place2 = Place(name="Market Square", country="Ukraine", city="Lviv",
                   description="It seems like all streets in the Old Town converge on this historic and hectic "
                               "central square surrounding Lviv’s Town Hall. Market Square heaves with locals, "
                               "tourists and street performers and the amount to see on this one plaza is almost "
                               "overwhelming: There are glorious townhouses on each side of the square, many from the "
                               "Renaissance (especially on the East side), and some with later Rococo designs. "
                               "Most contain bars, restaurants and cafes where you can watch the throngs, but there "
                               "are numerous museums and tasteful artisan shops. Rounding off the scene are four "
                               "classical fountains, one on each corner and depicting "
                               "Diana, Neptune, Adonis and Amphitrite.",
                   rate=5, image="https://cdn.thecrazytourist.com/wp-content/"
                                 "uploads/2018/08/ccimage-shutterstock_342499724.jpg", visible=True)
    place3 = Place(name="Pharmacy Museum", country="Ukraine", city="Lviv",
                   description="The “Under the Black Eagle Pharmacy” opened in 1735, and is the oldest pharmacy "
                               "still in business in the Ukraine. Since the 1960s it has lifted the lid on its old "
                               "laboratory, library, apothecary and 13 other rooms that date back almost 300 years. "
                               "The age of the building is clear as soon as you cross the threshold as the ceiling "
                               "is painted with images evoking earth, water, fire and air, the body’s “four humors”. "
                               "On the tour you’ll get to know the strange medicines prescribed for ailments centuries "
                               "ago. There’s a big stash of historic lab equipment like presses, scales, stills and "
                               "pestles and mortars, as well as cabinets laden with earthenware medicine jars and "
                               "antique books going back to the 1700s.",
                   rate=5,
                   image="https://cdn.thecrazytourist.com/"
                         "wp-content/uploads/2018/08/ccimage-shutterstock_666846613.jpg", visible=True)
    place4 = Place(name="Armenian Cathedral", country="Ukraine", city="Lviv",
                   description="There has been an Armenian community in Lviv since the 13th century, and it’s around "
                               "1,000-strong today after immigration during the Soviet Union. As the oldest church "
                               "in the city, the Armenian Cathedral was founded in the 1360s. The church has seen "
                               "a few changes due to fire, but the Byzantine layout and khachkars (engravings of "
                               "Armenian crosses) in the apse on the eastern side of the temple are from the earliest "
                               "period. The southern section of the arcaded courtyard outside is also historic and "
                               "dates to the 15th century. In the 1900s the church’s interior walls were painted with "
                               "bold Art Nouveau frescoes by the Polish artists "
                               "Józef Mehoffer and Jan Henryk de Rosen.",
                   rate=5, image="https://cdn.thecrazytourist.com/wp-content/uploads"
                                 "/2018/08/ccimage-shutterstock_1121748860.jpg", visible=True)
    place5 = Place(name="Lviv Arsenal", country="Ukraine", city="Lviv",
                   description="There’s a department of the Lviv Historical Museum at one of the city’s three "
                               "historic Arsenal buildings. It’s a stiff walk uphill, just east of the centre, "
                               "but will thrill anyone with a taste for old-school weaponry. The exhibition spans "
                               "1,000 years and 30 countries, and has blades and firearms that increase of varying "
                               "sophistication. Many of these pieces were crafted to be seen and come encrusted with "
                               "precious stones and inlaid with ivory and mother of pearl. One of a catalogue of "
                               "must-sees is a double-edged Ottoman sword from the 17th century, named “Zulqifar”. "
                               "There are also Polish maces from the high middle ages, an Italian Renaissance "
                               "ceremonial helmet, a Tatar shield from the 17th century and bronze canons forged "
                               "in Lviv in the 1500s and 1600s.",
                   rate=5, image="https://cdn.thecrazytourist.com/wp-content/"
                                 "uploads/2018/08/ccimage-shutterstock_1149754769.jpg", visible=True)
    place6 = Place(name="Dominican Church", country="Ukraine", city="Lviv",
                   description="Lviv has more than a hundred churches, but the Baroque Dominican Church to the "
                               "east of Market Square should be a priority. The present temple was completed in 1761, "
                               "and this plot has been occupied by a Dominican church of some kind since 1378. "
                               "Its distinguishing feature is an elongated ellipsoid dome bears a resemblance "
                               "to Vienna’s famed Karlskirche, built around 20 years before. Go in to stand under "
                               "that dome and see the pairs of sturdy Corinthian columns holding it up. After "
                               "a spell as a museum in Soviet times the church has been re-consecrated, and is "
                               "unusual in that you’re allowed to take photographs inside (within reason), and "
                               "because of the high number of weddings that take place here.",
                   rate=5, image="https://cdn.thecrazytourist.com/wp-content/"
                                 "uploads/2018/08/ccimage-shutterstock_1118954447.jpg", visible=True)
    place7 = Place(name="Armenian Street", country="Ukraine", city="Lviv",
                   description="After the Armenians were forced to flee from the Mongols in the 13th century, "
                               "many settled on Virmenska Street, also home to the Armenian Cathedral. In medieval "
                               "times the street was outside the city walls, while the Armenian community abided by "
                               "its own laws and grew wealthy from trade with the east. Now, although you need "
                               "to look hard to spot signs of Armenian heritage on Virmenska Street, it’s still one "
                               "of Lviv’s most enchanting streets, flanked by historic stone houses hosting cafes, "
                               "restaurants and galleries. And there are a hints of the Armenian community "
                               "in the wide portals of the houses, which was a common trait of Armenian architecture "
                               "up to the 1700s.",
                   rate=5,
                   image="https://cdn.thecrazytourist.com/wp-content/"
                         "uploads/2018/08/ccimage-shutterstock_650166007.jpg", visible=True)
    place8 = Place(name="High Castle", country="Ukraine", city="Lviv",
                   description="Watching over Lviv from its northeastern fringe is High Castle Hill, the perch for "
                               "the eponymous castle dating to 1250 but dismantled in the 19th century. The hill "
                               "crests at 413 metres, and setting off on foot from Market Square it takes about "
                               "25 minutes to reach the top. The path is perfectly walkable, if a little taxing on "
                               "the upper reaches, when the slope becomes very sharp. But a bit of persistence will "
                               "give you another sweeping view of Lviv, where you can compare the palaces, towers and "
                               "spires of old Lviv with the Soviet housing blocks of the suburbs. The castle is a "
                               "ruin today, and there’s not much left apart from a wall. But the journey is all about "
                               "the view and the vegetation at the top: Come just at sunrise in summer and you may "
                               "have it completely to yourself.",
                   rate=5, image="https://cdn.thecrazytourist.com/wp-content/"
                                 "uploads/2018/08/ccimage-shutterstock_1061659757.jpg", visible=True)
    place9 = Place(name="Lychakiv Cemetery", country="Ukraine", city="Lviv",
                   description="Since the 1500s, Lviv’s most prominent figures have been laid to rest at this "
                               "40-hectare cemetery that has now been recognised as a national reserve. Lychakiv "
                               "Cemetery is the equivalent to Père Lachaise or Highgate and is treasured not just "
                               "for its prestigious burials but the quality of the art that commemorates them. Laid "
                               "to rest here are Polish and Ukrainian members of the clergy, politicians, military "
                               "leaders, scientists, architects (like Zygmunt Gorgolewski), soloists, aviators, "
                               "surgeons and painters. For Poles the cemetery is poignant as the burial place of "
                               "the Lwów Eaglets, young militia members who were killed during "
                               "the Polish-Ukrainian War in 1918-1919.",
                   rate=5, image="https://cdn.thecrazytourist.com/wp-content/"
                                 "uploads/2018/08/ccimage-shutterstock_14336488.jpg", visible=True)
    place10 = Place(name="Museum of Folk Architecture and Rural Life", country="Ukraine", city="Lviv",
                    description="In the same district, on the eastern outskirts you can get a complete snapshot of "
                                "Ukrainian traditions and rural life without having to stray far from the city. "
                                "There are buses from the Arsenal stop (29, 36, 39 and 50) arriving at the attraction "
                                "in a matter of minutes.The museum has 124 buildings, scattered on a wooded hill and "
                                "relocated here from other parts of the country. A few of these buildings are open, "
                                "exhibiting tools, costumes and folk art, or hosting demonstrations of old-time "
                                "trades. The must-sees are the house from the Carpathian village of Oriavchyk, "
                                "dating to 1792, and the wooden church of St Nicholas from 1763, both brought "
                                "here in the 1930s.",
                    rate=5,
                    image="https://cdn.thecrazytourist.com/wp-content/"
                          "uploads/2018/08/ccimage-shutterstock_1083255287.jpg", visible=True)
    place11 = Place(name="House of Scientists", country="Ukraine", city="Lviv",
                    description="Once a casino and now an events venue for the Regional Union of Education and "
                                "Science, the House of Scientists is a shining piece of turn-of-the-century "
                                "architecture. The building was drawn up by the Viennese pair Fellner & Helmer who "
                                "built numerous landmarks across Central and Eastern Europe in this period. It was a "
                                "casino up to 1939 and had a salacious reputation, while during the Second World War "
                                "the Nazis used it to process prisoners for their camps. The architecture is in a "
                                "plush Neo-Baroque style and famed for the opulence of its interiors. You have to go "
                                "inside where there’s a staircase meticulously carved from oak illuminated by a "
                                "domed skylight. This beckons you up to the first floor to a beautiful library and "
                                "seven other rooms embellished with chandeliers, marble fireplaces, stuccowork and "
                                "period furniture.",
                    rate=5,
                    image="https://cdn.thecrazytourist.com/wp-content/"
                          "uploads/2018/08/ccimage-shutterstock_195532433.jpg", visible=True)
    place12 = Place(name="Chapel of the Boim Family", country="Ukraine", city="Lviv",
                    description="On the eastern edge of Cathedral square there’s a 17th-century Mannerist chapel "
                                "that has no equivalent in either Ukraine or the rest of Europe. The facade is "
                                "completely taken over by sandstone carvings, that may take a while to decipher. "
                                "On the lower tier are statues of the apostles St Peter and St Paul, in the middle "
                                "are cartouches with Latin inscriptions, while on the densely packed third tier are "
                                "scenes from the Passion. You can make out the Castigation, Christ Carrying the Cross "
                                "and the Crucifixion. There’s also loads of decoration crammed into the interior "
                                "n the form of intricate stuccowork. This is most impressive on the dome, lit by "
                                "an octagonal lantern and with 36 panels of sculptures representing "
                                "prophets, angels, the apostles and Jesus.",
                    rate=5,
                    image="https://cdn.thecrazytourist.com/wp-content/"
                          "uploads/2018/08/ccimage-shutterstock_626739452.jpg", visible=True)
    place13 = Place(name="St George’s Cathedral", country="Ukraine", city="Lviv",
                    description="This 18th-century Catholic cathedral looks out over Lviv from its namesake hill "
                                "on the west side of the city. It was built over 15 years up to 1760 and its exterior "
                                "ornamentation is as rich as it gets. Against walls painted a pale yellow there are "
                                "lavish Rococo pilasters, sculptures, balustrades and highly ornate mouldings. "
                                "Above the portal stand two dominant statues, one of St Leo and the other of "
                                "St Athanasius, both the work of the Czech sculptor Johann Georg Pinsel. "
                                "After all that drama the interior is a lot more discreet, but there are some "
                                "fascinating things to see, like a “wonder-working” icon of Mary from the 1600s, "
                                "and tombs for some eminent figures of the Ukrainian Greek-Catholic church.",
                    rate=5, image="https://cdn.thecrazytourist.com/wp-content/"
                                  "uploads/2018/08/ccimage-shutterstock_225185485.jpg", visible=True)
    place14 = Place(name="City Hall", country="Ukraine", city="Lviv",
                    description="The seat of Lviv’s city council is a medley of buildings, the oldest dating to the "
                                "14th century. The oldest elements are towards the centre, while the western side is "
                                "from the turn of the 16th century. The City Hall was capped with a new, "
                                "650-metre Renaissance Revival tower in the 1830s. As long as you’ve got the energy, "
                                "a trip to the top should be one of the first things you do in Lviv, because it’s the "
                                "easiest way to get your bearings. This is no simple task though, as just to get "
                                "to the ticket office you have climb 103 steps. And after that you’ve got to tackle "
                                "another 305 before you come to that vista of the city and its famous hills.",
                    rate=5, image="https://cdn.thecrazytourist.com/wp-content/"
                                  "uploads/2018/08/ccimage-shutterstock_298741211.jpg", visible=True)
    place15 = Place(name="Kryivka", country="Ukraine", city="Lviv",
                    description="If you happen to be around Monument to Leopold von Sacher-Masoch, visit this "
                                "restaurant. Ukrainian cuisine is served at Kryivka. You can always degust tasty "
                                "pelmeni, poutine and borsch at this place. Try good Compote, crepes and spoon sweets. "
                                "A collection of delicious craft beer, ale or cordial is recommended to guests. You "
                                "will hardly forget great latte, tea or kinnie that you can try. The homely "
                                "atmosphere of this spot allows customers to relax after a hard working day. "
                                "The enjoyable service and the gracious staff are big advantages of this restaurant. "
                                "You will appreciate affordable prices. Based on the visitors' opinions, "
                                "the decor is nice.",
                    rate=5,
                    image="https://i.pinimg.com/originals/6f/a5/e7/"
                          "6fa5e70bddce0deac435ca68091f5453.jpg", visible=True)
    place16 = Place(name="Karpatia", country="Ukraine", city="Mukachevo",
                    description="'Karpatiya' is one of the largest health and entertainment complexes of Ukraine, "
                                "which combines modern attractions, thermal pools, SPA and "
                                "a fabulous atmosphere.",
                    rate=4,
                    image="http://www.mukachevo.net/Content/img/news/2744/p_2744697_14_slidertop2.jpg", visible=True)
    place17 = Place(name="Aquapark Pliazh", country="Ukraine", city="Lviv",
                    description="Water park 'Plyazh' in Lviv is the largest indoor water park in Western Ukraine. The "
                                "total area of ​​the complex is 14 thousand square meters. m. and combines the "
                                "conditions for various types of recreation, both recreational and sports and health. "
                                "The most modern equipment is responsible for the high level of safety for those "
                                "vacationing in the water complex, all attractions have quality certificates, and the "
                                "latest water purification systems are installed in the pools.",
                    rate=4,
                    image="https://akvapark-lviv.virtual.ua/images/374591/akvapark-lviv.virtual.ua_007.jpg",
                    visible=True)
    place18 = Place(name="Mount Hoverla",
                    country="Ukraine", city="-",
                    description="Hoverla is the highest peak of the Ukrainian Carpathians and the highest point "
                                "of Ukraine, the height of which is 2061 m above sea level. It is located in the "
                                "Chornohora mountain range, on the border of the Yaremchan city council of the "
                                "Ivano-Frankivsk region and the Rakhiv district of the Zakarpattia region, 17 "
                                "kilometers from the border with Romania.",
                    rate=5,
                    image="https://f.discover.ua/location/2105/hPjTC.jpg",
                    visible=True)
    place19 = Place(name="Mount Khomyak", country="Ukraine", city="Tatariv",
                    description="The peak with a mild and funny name - Mount Khomyak (1542 m), turns out to have long "
                                "been an attractive place for beginner tourists and simply for those who do not want "
                                "to strain too much during the ascent, but at the same time hope to see all the beauty "
                                "of the peak landscapes peaks",
                    rate=5,
                    image="https://www.v-mandry.com/wp-content/uploads/2017/10/523010_original-1024x634.jpg",
                    visible=True)
    place20 = Place(name="Mount Makovitsa", country="Ukraine", city="Yaremche",
                    description="Makovitsa is one of the highest peaks in the vicinity of the city of Yaremche. "
                                "The northern and northwestern slopes are steep, the southern and southwestern slopes "
                                "are gentler. The foothills of the mountain, especially the northwestern and middle "
                                "parts, except for steep screes, are covered with almost continuous forests, the top "
                                "- sparse shrubs and individual trees. Areas free from forest are rich in grass cover.",
                    rate=4,
                    image="https://i.pinimg.com/originals/07/a4/bc/07a4bc83fe738ae66ca23e3c88c74a0c.jpg",
                    visible=True)
    place21 = Place(name="Mount Yagidna", country="Ukraine", city="Mykulychyn",
                    description="A hike to Mount Yagidna is an ideal option for an easy walk through the Carpathians. "
                                "The road is mostly forested and has almost no difficult steep climbs. There is a "
                                "possibility of descent both to the starting point — to the village. Mykulychyn, and "
                                "to Tatarov. At the same time, the total route distance is unchanged - about 15 km. "
                                "Depending on weather conditions and physical fitness, the route can be completed "
                                "much faster. The time of passing through the snow in winter is 7 hours. The great "
                                "advantage of Yagidnaya is its suitability for hiking at any time of the year. If "
                                "desired, the route can be extended by spending the night in the forest of Lisniv, or "
                                "continue along the Lisniv ridge to Mount Chornyi Pogar (1,266 m) and reach Vorokhta "
                                "or descend all the way to Kryvopilly.",
                    rate=4,
                    image="https://1.bp.blogspot.com/-sz1QSbP-zTc/WDBG7CoTSHI/AAAAAAAAJ1A/ZhA6GFnI0lkcft_"
                          "soPfyLiegOOZQ08lswCLcB/s640/DSC_0553-1.jpg",
                    visible=True)
    place22 = Place(name="Mount Parashka", country="Ukraine", city="Korchyn",
                    description="Mount Parashka (another name is Paraska), the height of which is 1268.5 m above "
                                "sea level, is located in the Ukrainian Carpathians in the Skoliv Beskydy. This is "
                                "the highest peak of the Parashka mountain range. The mountain is located on the "
                                "territory of the 'Skolivski Beskydy' National Nature Park. From the top of "
                                "Parashka there are wonderful views that attract a large number of tourists. "
                                "On a sunny day, you can see the village of Korchyn, the cities of Skole, Stryi, "
                                "Mykolaiv, and Lviv from the mountain.",
                    rate=4,
                    image="https://1.bp.blogspot.com/-fjWHP2rB7iQ/VVnzr4N0d7I/AAAAAAAAAbw/wvrVVrPcZ4o/s1600/2685.jpg",
                    visible=True)
    place23 = Place(name="Bukovel Bike Park", country="Ukraine", city="Bukovel",
                    description="Routes of varying complexity level with springboards, narrow crossings and natural "
                                "obstacles in the wild forest: a unique enviromnent for everyone willing to improve "
                                "their mountain bike skills. Today, our bike park is the only place in Ukraine that "
                                "is fully prepared for extreme downhill. At the moment we have 2 slopes open: 'blue' "
                                "for beginner riders and 'black' route for pros.",
                    rate=5,
                    image="https://i.ytimg.com/vi/IerV_awZ7Fc/maxresdefault.jpg",
                    visible=True)
    place24 = Place(name="Sykhivsky Bike Park", country="Ukraine", city="Lviv",
                    description="Sykhivsky Bike Park is a bike park on the territory of the Sykhivsky park. "
                                "This is the only bicycle park in Ukraine that combines all the infrastructure "
                                "solutions for lovers of sports and tourist bicycle recreation.",
                    rate=4,
                    image="https://content.26in.fr/p/pictures/4/9/7/49725/1d9d1c-9.jpg",
                    visible=True)
    place25 = Place(name="Bryukhovychi Bike Park", country="Ukraine", city="Lviv",
                    description="Bryukhovychi Bike Park is a bike park on the territory of the Bryukhovychi forest. "
                                "This is the only bicycle park in Ukraine that combines all the infrastructure "
                                "solutions for lovers of sports and tourist bicycle recreation.",
                    rate=4,
                    image="https://i.ytimg.com/vi/zN5Sx8Kk6vk/maxresdefault.jpg",
                    visible=True)
    place26 = Place(name="Cheremosh river", country="Ukraine", city="Cheremosh",
                    description="Cheremosh is the sacred river of the Hutsuls, which connects their region with the "
                                "whole of Ukraine, and then with the world. After all, its waters flow into the Black "
                                "Sea. And they flow from under the Palenytsia, Komenova and Komen mountains, which in "
                                "their shape really resemble the chimneys of Hutsul furnaces. The names of these "
                                "mountains have not yet been solved by researchers. Hutsuls call Cheremosh the "
                                "faithful son of the Carpathians, who, having been born in the mountains, lives here "
                                "among them, and dies here, falling into the Prut. And it is born from the confluence "
                                "of two rivers - Black and White Cheremosh. White, which, according to pagan beliefs, "
                                "carries its waters from the world of Right - the world of good gods. Black - from the "
                                "dangerous world of Navi, the place of the Underworld spirits. In fact, the waters of "
                                "the White Cheremosh, if you look at them from the bottom upstream, really seem white, "
                                "which is the origin of the name of the river. The Black Cheremosh, flowing past the "
                                "mountains, erodes them and enriches them with calcium. Therefore, its water acquires "
                                "a dark color.",
                    rate=5,
                    image="https://skyta.com.ua/trash/statica/0/f76a65b24818f95a2525ba0be8729865_600x1000.jpg",
                    visible=True)
    place27 = Place(name="SKA Velotrek", country="Ukraine", city="Lviv",
                    description="Track and field arena with bicycle track (better known as SKA Velotrek) is a sports "
                                "facility in Lviv that specializes in cycling and track and field competitions. It is "
                                "the only indoor cycling track in Ukraine. Located on the street Kleparivska, 39a. "
                                "Opened in 1980. It is part of the educational and sports base of summer sports of "
                                "the IOU.",
                    rate=4,
                    image="https://internet-bilet.ua/images/room_header_photo/size3/hph_1487841574_58aea9265efed.jpg",
                    visible=True)

    db.session.add_all([place1, place2, place3, place4, place5,
                        place6, place7, place8, place9, place10,
                        place11, place12, place13, place14, place15])
    db.session.commit()
    db.session.add_all([place16, place17, place18, place19, place20,
                        place21, place22, place23, place24, place25,
                        place26, place27])
    db.session.commit()

    place_season1 = PlaceSeason(place_id=place1.id, season_id=season1.id)
    place_season2 = PlaceSeason(place_id=place1.id, season_id=season2.id)
    place_season3 = PlaceSeason(place_id=place1.id, season_id=season3.id)
    place_season4 = PlaceSeason(place_id=place1.id, season_id=season4.id)
    place_activity1 = PlaceActivity(place_id=place1.id, activity_id=activity1.id)

    place_season5 = PlaceSeason(place_id=place2.id, season_id=season1.id)
    place_season6 = PlaceSeason(place_id=place2.id, season_id=season2.id)
    place_season7 = PlaceSeason(place_id=place2.id, season_id=season3.id)
    place_season8 = PlaceSeason(place_id=place2.id, season_id=season4.id)
    place_activity2 = PlaceActivity(place_id=place2.id, activity_id=activity1.id)

    place_season9 = PlaceSeason(place_id=place3.id, season_id=season1.id)
    place_season10 = PlaceSeason(place_id=place3.id, season_id=season2.id)
    place_season11 = PlaceSeason(place_id=place3.id, season_id=season3.id)
    place_season12 = PlaceSeason(place_id=place3.id, season_id=season4.id)
    place_activity3 = PlaceActivity(place_id=place3.id, activity_id=activity1.id)

    place_season13 = PlaceSeason(place_id=place4.id, season_id=season1.id)
    place_season14 = PlaceSeason(place_id=place4.id, season_id=season2.id)
    place_season15 = PlaceSeason(place_id=place4.id, season_id=season3.id)
    place_season16 = PlaceSeason(place_id=place4.id, season_id=season4.id)
    place_activity4 = PlaceActivity(place_id=place4.id, activity_id=activity1.id)

    place_season17 = PlaceSeason(place_id=place5.id, season_id=season1.id)
    place_season18 = PlaceSeason(place_id=place5.id, season_id=season2.id)
    place_season19 = PlaceSeason(place_id=place5.id, season_id=season3.id)
    place_season20 = PlaceSeason(place_id=place5.id, season_id=season4.id)
    place_activity5 = PlaceActivity(place_id=place5.id, activity_id=activity1.id)

    place_season21 = PlaceSeason(place_id=place6.id, season_id=season1.id)
    place_season22 = PlaceSeason(place_id=place6.id, season_id=season2.id)
    place_season23 = PlaceSeason(place_id=place6.id, season_id=season3.id)
    place_season24 = PlaceSeason(place_id=place6.id, season_id=season4.id)
    place_activity6 = PlaceActivity(place_id=place6.id, activity_id=activity1.id)

    place_season25 = PlaceSeason(place_id=place7.id, season_id=season1.id)
    place_season26 = PlaceSeason(place_id=place7.id, season_id=season2.id)
    place_season27 = PlaceSeason(place_id=place7.id, season_id=season3.id)
    place_season28 = PlaceSeason(place_id=place7.id, season_id=season4.id)
    place_activity7 = PlaceActivity(place_id=place7.id, activity_id=activity1.id)

    place_season29 = PlaceSeason(place_id=place8.id, season_id=season1.id)
    place_season30 = PlaceSeason(place_id=place8.id, season_id=season2.id)
    place_season31 = PlaceSeason(place_id=place8.id, season_id=season3.id)
    place_season32 = PlaceSeason(place_id=place8.id, season_id=season4.id)
    place_activity8 = PlaceActivity(place_id=place8.id, activity_id=activity1.id)

    place_season33 = PlaceSeason(place_id=place9.id, season_id=season1.id)
    place_season34 = PlaceSeason(place_id=place9.id, season_id=season2.id)
    place_season35 = PlaceSeason(place_id=place9.id, season_id=season3.id)
    place_season36 = PlaceSeason(place_id=place9.id, season_id=season4.id)
    place_activity9 = PlaceActivity(place_id=place9.id, activity_id=activity1.id)

    place_season37 = PlaceSeason(place_id=place10.id, season_id=season1.id)
    place_season38 = PlaceSeason(place_id=place10.id, season_id=season2.id)
    place_season39 = PlaceSeason(place_id=place10.id, season_id=season3.id)
    place_season40 = PlaceSeason(place_id=place10.id, season_id=season4.id)
    place_activity10 = PlaceActivity(place_id=place10.id, activity_id=activity1.id)

    place_season41 = PlaceSeason(place_id=place11.id, season_id=season1.id)
    place_season42 = PlaceSeason(place_id=place11.id, season_id=season2.id)
    place_season43 = PlaceSeason(place_id=place11.id, season_id=season3.id)
    place_season44 = PlaceSeason(place_id=place11.id, season_id=season4.id)
    place_activity11 = PlaceActivity(place_id=place11.id, activity_id=activity1.id)

    place_season45 = PlaceSeason(place_id=place12.id, season_id=season1.id)
    place_season46 = PlaceSeason(place_id=place12.id, season_id=season2.id)
    place_season47 = PlaceSeason(place_id=place12.id, season_id=season3.id)
    place_season48 = PlaceSeason(place_id=place12.id, season_id=season4.id)
    place_activity12 = PlaceActivity(place_id=place12.id, activity_id=activity1.id)

    place_season49 = PlaceSeason(place_id=place13.id, season_id=season1.id)
    place_season50 = PlaceSeason(place_id=place13.id, season_id=season2.id)
    place_season51 = PlaceSeason(place_id=place13.id, season_id=season3.id)
    place_season52 = PlaceSeason(place_id=place13.id, season_id=season4.id)
    place_activity13 = PlaceActivity(place_id=place13.id, activity_id=activity1.id)

    place_season53 = PlaceSeason(place_id=place14.id, season_id=season1.id)
    place_season54 = PlaceSeason(place_id=place14.id, season_id=season2.id)
    place_season55 = PlaceSeason(place_id=place14.id, season_id=season3.id)
    place_season56 = PlaceSeason(place_id=place14.id, season_id=season4.id)
    place_activity14 = PlaceActivity(place_id=place14.id, activity_id=activity1.id)

    place_season57 = PlaceSeason(place_id=place15.id, season_id=season1.id)
    place_season58 = PlaceSeason(place_id=place15.id, season_id=season2.id)
    place_season59 = PlaceSeason(place_id=place15.id, season_id=season3.id)
    place_season60 = PlaceSeason(place_id=place15.id, season_id=season4.id)
    place_activity15 = PlaceActivity(place_id=place15.id, activity_id=activity7.id)

    place_activity16 = PlaceActivity(place_id=place16.id, activity_id=activity6.id)
    place_activity17 = PlaceActivity(place_id=place17.id, activity_id=activity6.id)
    place_activity18 = PlaceActivity(place_id=place18.id, activity_id=activity2.id)
    place_activity19 = PlaceActivity(place_id=place19.id, activity_id=activity2.id)
    place_activity20 = PlaceActivity(place_id=place20.id, activity_id=activity2.id)
    place_activity21 = PlaceActivity(place_id=place21.id, activity_id=activity2.id)
    place_activity22 = PlaceActivity(place_id=place22.id, activity_id=activity2.id)
    place_activity23 = PlaceActivity(place_id=place23.id, activity_id=activity3.id)
    place_activity23_a = PlaceActivity(place_id=place23.id, activity_id=activity5.id)
    place_activity24 = PlaceActivity(place_id=place24.id, activity_id=activity3.id)
    place_activity25 = PlaceActivity(place_id=place25.id, activity_id=activity3.id)
    place_activity26 = PlaceActivity(place_id=place26.id, activity_id=activity4.id)
    place_activity27 = PlaceActivity(place_id=place27.id, activity_id=activity5.id)
    # activity1 = Activity(name="Sightseeing")
    # activity2 = Activity(name="Hiking")
    # activity3 = Activity(name="Mountain biking")
    # activity4 = Activity(name="Rowing")
    # activity5 = Activity(name="Cycling")
    # activity6 = Activity(name="Swimming")
    # activity7 = Activity(name="Eating out")
    db.session.add_all([place_season1, place_season2, place_season3, place_season4, place_season5,
                        place_season6, place_season7, place_season8, place_season9, place_season10,
                        place_season11, place_season12, place_season13, place_season14, place_season15,
                        place_season16, place_season17, place_season18, place_season19, place_season20,
                        place_season21, place_season22, place_season23, place_season24, place_season25,
                        place_season26, place_season27, place_season28, place_season29, place_season30,
                        place_season31, place_season32, place_season33, place_season34, place_season35,
                        place_season36, place_season37, place_season38, place_season39, place_season40,
                        place_season41, place_season42, place_season43, place_season44, place_season45,
                        place_season46, place_season47, place_season48, place_season49, place_season50,
                        place_season51, place_season52, place_season53, place_season54, place_season55,
                        place_season56,  place_season57, place_season58, place_season59, place_season60,
                        place_activity1, place_activity2, place_activity3, place_activity4, place_activity5,
                        place_activity6, place_activity7, place_activity8, place_activity9, place_activity10,
                        place_activity11, place_activity12, place_activity13, place_activity14, place_activity15,
                        place_activity16, place_activity17, place_activity18, place_activity19, place_activity20,
                        place_activity21, place_activity22, place_activity23, place_activity24, place_activity25,
                        place_activity26, place_activity27, place_activity23_a])
    db.session.commit()

    photo_1_1 = PlacePhoto(image='https://th.bing.com/th/id/R.3f616a6aaf8dfed672d41440c6ca20a6?rik=Frt4aVMzEw6qMQ&riu='
                                 'http%3a%2f%2fitinery.com.ua%2fimg%2fobjects%2fobject_20170708_020345.jpg&ehk=4SBinni'
                                 'D5SxQLHt8oP5U6K2MKmF50W27Prd0xeRpIfw%3d&risl=&pid=ImgRaw&r=0',
                           place_id=place1.id)
    photo_1_2 = PlacePhoto(image='https://th.bing.com/th/id/R.87e5136cc7ce36acad768cd89196a153?'
                                 'rik=o5qPx%2bwLSo%2bTwA&pid=ImgRaw&r=0',
                           place_id=place1.id)
    photo_1_3 = PlacePhoto(image='https://lwow.info/wp-content/uploads/2014/05/020101030.jpg',
                           place_id=place1.id)
    photo_1_4 = PlacePhoto(image='https://www.tatilinburada.com/picture0x0/3.ara-tatil-ozel-thy-ile-klasik-ukrayna'
                                 '-turu-promo-fiyat-!.jpg',
                           place_id=place1.id)
    photo_1_5 = PlacePhoto(image='https://opera.lviv.ua/wp-content/uploads/2017/09/8-3-1024x683.jpg',
                           place_id=place1.id)
    # "https://i.pinimg.com/236x/0d/7b/6d/0d7b6d9c194370e12d6b5e249df60bab.jpg"
    # "https://i.pinimg.com/236x/da/a7/0f/daa70ffbca353610e8f336144ae9e541.jpg"
    # "https://i.pinimg.com/236x/2c/59/10/2c5910bd003d30126137366c58fa32d5.jpg"
    # "https://i.pinimg.com/236x/aa/67/7d/aa677d678a8311b8f2adf0da88422147.jpg"
    # "https://i.pinimg.com/236x/ae/cd/66/aecd664acde6ab6599e3b0b30d530bbf.jpg"
    # 'https://th.bing.com/th/id/R.7d83817b2745adf33a609462fa1839f4?rik=Rth505W8hkHYJw&pid=ImgRaw&r=0'

    photo_2_1 = PlacePhoto(image='https://i.pinimg.com/236x/02/cf/63/02cf6373672b8d5c75ab85eb959743ad.jpg',
                           place_id=place2.id)
    photo_2_2 = PlacePhoto(image='https://i.pinimg.com/236x/c8/02/69/c802695adc58871966e866a7d95c9c35.jpg',
                           place_id=place2.id)
    photo_2_3 = PlacePhoto(image='https://i.pinimg.com/236x/e7/a5/38/e7a538bbbcc82cef586fa8f6e8535dc6.jpg',
                           place_id=place2.id)
    photo_2_4 = PlacePhoto(image='https://i.pinimg.com/236x/0f/3b/62/0f3b62c08cdff9c35730bca74f2314a2.jpg',
                           place_id=place2.id)
    photo_2_5 = PlacePhoto(image='https://i.pinimg.com/236x/19/18/00/191800d804b6c00d5d88ac1c2c0a9a75.jpg',
                           place_id=place2.id)

    photo_3_1 = PlacePhoto(image='https://i.pinimg.com/236x/d2/7d/21/d27d21d3219ff543f39ebb1faddf42e9.jpg',
                           place_id=place3.id)
    photo_3_2 = PlacePhoto(image='https://i.pinimg.com/236x/af/46/35/af463562ade90ef7bd1cf21b5c269a8b.jpg',
                           place_id=place3.id)
    photo_3_3 = PlacePhoto(image='https://i.pinimg.com/236x/c5/22/d9/c522d9ef9f78d1bbca2133677492c1b6.jpg',
                           place_id=place3.id)
    photo_3_4 = PlacePhoto(image='https://i.pinimg.com/236x/24/c9/66/24c9667124a9e50d91fe96143a3bea59.jpg',
                           place_id=place3.id)
    photo_3_5 = PlacePhoto(image='https://i.pinimg.com/236x/17/be/d6/17bed6989d4d3f664f45925d780440d3.jpg',
                           place_id=place3.id)

    photo_4_1 = PlacePhoto(image='https://i.pinimg.com/236x/16/0a/22/160a220b82ae907f0acb947949bfe8a9.jpg',
                           place_id=place4.id)
    photo_4_2 = PlacePhoto(image='https://i.pinimg.com/236x/fd/34/ff/fd34ffa2b49b19e5cab2867ed6cec35a.jpg',
                           place_id=place4.id)
    photo_4_3 = PlacePhoto(image='https://i.pinimg.com/236x/1c/1d/94/1c1d94ba77eb09de61d6af62f21d916b.jpg',
                           place_id=place4.id)
    photo_4_4 = PlacePhoto(image='https://i.pinimg.com/236x/a9/f8/45/a9f845c7b19625f177b491d5480b4214.jpg',
                           place_id=place4.id)
    photo_4_5 = PlacePhoto(image='https://i.pinimg.com/236x/53/df/70/53df7051c062892076943b36882e4f4a.jpg',
                           place_id=place4.id)

    photo_5_1 = PlacePhoto(image='https://i.pinimg.com/236x/0d/24/46/0d24462187a280540df1ee2374732f39.jpg',
                           place_id=place5.id)
    photo_5_2 = PlacePhoto(image='https://i.pinimg.com/236x/ce/0e/7a/ce0e7a1b7e7a493dbd0e90f7cfde1f32.jpg',
                           place_id=place5.id)
    photo_5_3 = PlacePhoto(image='https://i.pinimg.com/236x/cb/32/02/cb3202d29d7afa218ae2a382b0aff04d.jpg',
                           place_id=place5.id)
    photo_5_4 = PlacePhoto(image='https://i.pinimg.com/236x/50/35/82/5035824be9d9c08c336043758c0c9b6c.jpg',
                           place_id=place5.id)
    photo_5_5 = PlacePhoto(image='https://i.pinimg.com/236x/c6/92/41/c69241583fe5aacf91ea953673a5a576.jpg',
                           place_id=place5.id)

    photo_6_1 = PlacePhoto(image='https://i.pinimg.com/236x/4c/ff/c5/4cffc55c4a05539e78f66ecf56daeabd.jpg',
                           place_id=place6.id)
    photo_6_2 = PlacePhoto(image='https://i.pinimg.com/236x/d2/25/38/d225385fc0e998b6aa1e694816c8d26e.jpg',
                           place_id=place6.id)
    photo_6_3 = PlacePhoto(image='https://i.pinimg.com/236x/da/15/c4/da15c442ac035362dd7bd51a2fc99f92.jpg',
                           place_id=place6.id)
    photo_6_4 = PlacePhoto(image='https://i.pinimg.com/236x/bd/51/f9/bd51f9117990b2877230768e9a2c9794.jpg',
                           place_id=place6.id)
    photo_6_5 = PlacePhoto(image='https://i.pinimg.com/236x/1c/02/5c/1c025c39d21852db8c2469bbcb2a7cc8.jpg',
                           place_id=place6.id)

    photo_7_1 = PlacePhoto(image='https://i.pinimg.com/236x/53/df/70/53df7051c062892076943b36882e4f4a.jpg',
                           place_id=place7.id)
    photo_7_2 = PlacePhoto(image='https://i.pinimg.com/236x/10/d5/c8/10d5c808a23ead55828da4aa918a4f77.jpg',
                           place_id=place7.id)
    photo_7_3 = PlacePhoto(image='https://i.pinimg.com/236x/34/0d/a3/340da3f183e1ae11c4da0a336ecb0914.jpg',
                           place_id=place7.id)
    photo_7_4 = PlacePhoto(image='https://i.pinimg.com/236x/57/b2/d5/57b2d5ec4cb0fedacd0f0c2952b4c540.jpg',
                           place_id=place7.id)
    photo_7_5 = PlacePhoto(image='https://i.pinimg.com/236x/a6/5d/c5/a65dc5571bd6b4f6294f223d8e88fd86.jpg',
                           place_id=place7.id)

    photo_8_1 = PlacePhoto(image='https://i.pinimg.com/236x/2d/07/d4/2d07d4eb984967e20fc2d412891fc543.jpg',
                           place_id=place8.id)
    photo_8_2 = PlacePhoto(image='https://i.pinimg.com/236x/7e/01/57/7e0157df6087528b3d1f7eca32326abb.jpg',
                           place_id=place8.id)
    photo_8_3 = PlacePhoto(image='https://i.pinimg.com/236x/14/bc/75/14bc752f5a954d35e8327a251b6fabd6.jpg',
                           place_id=place8.id)
    photo_8_4 = PlacePhoto(image='https://i.pinimg.com/236x/f6/9d/ef/f69def430aba032f1fb935181c724628.jpg',
                           place_id=place8.id)
    photo_8_5 = PlacePhoto(image='https://i.pinimg.com/236x/37/47/b6/3747b685675731405cc49c85a93d5708.jpg',
                           place_id=place8.id)

    photo_9_1 = PlacePhoto(image='https://i.pinimg.com/236x/4d/d4/70/4dd4702744a68ba14896f092aaddc313.jpg',
                           place_id=place9.id)
    photo_9_2 = PlacePhoto(image='https://i.pinimg.com/236x/ea/68/4d/ea684d0e620bf8bd83ad54c65aa61064.jpg',
                           place_id=place9.id)
    photo_9_3 = PlacePhoto(image='https://i.pinimg.com/236x/8f/a4/c4/8fa4c4ec8d354829fc215efd78d348f9.jpg',
                           place_id=place9.id)
    photo_9_4 = PlacePhoto(image='https://i.pinimg.com/236x/e1/6b/fe/e16bfe76a228fabd137bbe41d5d20dfb.jpg',
                           place_id=place9.id)
    photo_9_5 = PlacePhoto(image='https://i.pinimg.com/236x/0a/76/19/0a761978ddfa60a10536bcffa5abcc68.jpg',
                           place_id=place9.id)

    photo_10_1 = PlacePhoto(image='https://i.pinimg.com/236x/c2/bb/af/c2bbafc54ac46bf6b4d0628bc1be9f3a.jpg',
                            place_id=place10.id)
    photo_10_2 = PlacePhoto(image='https://i.pinimg.com/236x/aa/4b/38/aa4b38a4297a4cdd040b5347ebbf3291.jpg',
                            place_id=place10.id)
    photo_10_3 = PlacePhoto(image='https://i.pinimg.com/236x/b2/25/b9/b225b96ea5966b398bcef6e4404d9c36.jpg',
                            place_id=place10.id)
    photo_10_4 = PlacePhoto(image='https://i.pinimg.com/236x/d6/14/7c/d6147cd4d9263612a1bea40e86aad916.jpg',
                            place_id=place10.id)
    photo_10_5 = PlacePhoto(image='https://i.pinimg.com/236x/3f/56/57/3f56573fce4c46289553191d9a3d5b3c.jpg',
                            place_id=place10.id)

    photo_11_1 = PlacePhoto(image='https://i.pinimg.com/236x/02/be/a7/02bea731717f9efd6a724312ca2a7380.jpg',
                            place_id=place11.id)
    photo_11_2 = PlacePhoto(image='https://i.pinimg.com/236x/33/56/17/335617354ec242bef67196348ffc291a.jpg',
                            place_id=place11.id)
    photo_11_3 = PlacePhoto(image='https://i.pinimg.com/236x/7f/8b/6c/7f8b6c9221a2c1d0dc53cd6688e876ec.jpg',
                            place_id=place11.id)
    photo_11_4 = PlacePhoto(image='https://i.pinimg.com/236x/ef/77/63/ef77639a1697bf8e5fdcc78e70ebd3e7.jpg',
                            place_id=place11.id)
    photo_11_5 = PlacePhoto(image='https://i.pinimg.com/236x/ec/79/b7/ec79b7e7b42b04cbd5529260704d2426.jpg',
                            place_id=place11.id)

    photo_12_1 = PlacePhoto(image='https://i.pinimg.com/236x/42/55/97/42559709d41ee8c07fd1448dc611e8df.jpg',
                            place_id=place12.id)
    photo_12_2 = PlacePhoto(image='https://i.pinimg.com/236x/f6/ae/3c/f6ae3ca5dfb3e150f8dcf14f0d35b8d2.jpg',
                            place_id=place12.id)
    photo_12_3 = PlacePhoto(image='https://i.pinimg.com/236x/c0/ea/dc/c0eadc20bdfc9e8d02a39632302b29ea.jpg',
                            place_id=place12.id)
    photo_12_4 = PlacePhoto(image='https://i.pinimg.com/236x/9d/7b/ea/9d7beab4839e9b56a2dd68268ede2ca3.jpg',
                            place_id=place12.id)
    photo_12_5 = PlacePhoto(image='https://i.pinimg.com/236x/ba/1a/d2/ba1ad21975389c4c2a7ebe89281a17b3.jpg',
                            place_id=place12.id)

    photo_13_1 = PlacePhoto(image='https://i.pinimg.com/236x/c1/68/a4/c168a43aee64b3225bf95636cf7c7557.jpg',
                            place_id=place13.id)
    photo_13_2 = PlacePhoto(image='https://i.pinimg.com/236x/f1/72/79/f172797b0fdd9009161d9302fbec9795.jpg',
                            place_id=place13.id)
    photo_13_3 = PlacePhoto(image='https://i.pinimg.com/236x/46/93/aa/4693aacd72ded1d999df71b3d4dad6f9.jpg',
                            place_id=place13.id)
    photo_13_4 = PlacePhoto(image='https://i.pinimg.com/236x/b3/70/d7/b370d76d9f7addd755ecdbaec06442b0.jpg',
                            place_id=place13.id)
    photo_13_5 = PlacePhoto(image='https://i.pinimg.com/236x/dd/71/90/dd7190845113be5ce839e911dc74ffeb.jpg',
                            place_id=place13.id)

    photo_14_1 = PlacePhoto(image='https://i.pinimg.com/236x/39/0d/13/390d134ecba8dda6aa913f8fb04ba122.jpg',
                            place_id=place14.id)
    photo_14_2 = PlacePhoto(image='https://i.pinimg.com/236x/7a/bd/92/7abd9225743a5872fd2f1f1b40085e5a.jpg',
                            place_id=place14.id)
    photo_14_3 = PlacePhoto(image='https://i.pinimg.com/236x/40/f3/ef/40f3efb173986fc996e9290727ae50f0.jpg',
                            place_id=place14.id)
    photo_14_4 = PlacePhoto(image='https://i.pinimg.com/236x/87/cd/a4/87cda49fbbb17f0d05c1092c89a0b7a2.jpg',
                            place_id=place14.id)
    photo_14_5 = PlacePhoto(image='https://i.pinimg.com/236x/fa/77/2b/fa772bf3aa26b692c6c637ec0cb9c0fc.jpg',
                            place_id=place14.id)

    photo_15_1 = PlacePhoto(image='', place_id=place15.id)
    photo_15_2 = PlacePhoto(image='https://i.pinimg.com/236x/ad/ae/2b/adae2b5dc3a521ac0e3c542ba8313ac9.jpg',
                            place_id=place15.id)
    photo_15_3 = PlacePhoto(image='https://topclub.ua/images/uploads/kryjivka_1.jpg', place_id=place15.id)
    photo_15_4 = PlacePhoto(image='https://tamtour.com.ua/local/image/556/009/985633-900@.jpg', place_id=place15.id)
    photo_15_5 = PlacePhoto(image='https://i.pinimg.com/originals/6f/a5/e7/6fa5e70bddce0deac435ca68091f5453.jpg',
                            place_id=place15.id)

    photo_16_1 = PlacePhoto(image='https://termalfurdok.com/wp-content/uploads/2021/07/'
                                  'aquapark_munkacs_karpatia-768x512.jpg', place_id=place16.id)
    photo_16_2 = PlacePhoto(image='https://pmg.ua/uploads/2021-07/15/60f0286c116f8-217850216_'
                                  '4178244302269350_61124550066988604_njpg.jpg', place_id=place16.id)
    photo_16_3 = PlacePhoto(image='https://tourinform.org.ua/wp-content/uploads/2021/08/217767802_'
                                  '175684357945778_6130320438056643643_n.jpg', place_id=place16.id)
    photo_16_4 = PlacePhoto(image='https://tourinform.org.ua/wp-content/uploads/2021/08/218087985_'
                                  '176791931168354_3558588235874281532_n.jpg', place_id=place16.id)
    photo_16_5 = PlacePhoto(image='https://tourinform.org.ua/wp-content/uploads/2021/08/224695943_'
                                  '184966847017529_3660725107713672017_n.jpg', place_id=place16.id)

    photo_17_1 = PlacePhoto(image='https://akvapark-lviv.virtual.ua/images/374587/akvapark-lviv.virtual.ua_003.jpg',
                            place_id=place17.id)
    photo_17_2 = PlacePhoto(image='https://akvapark-lviv.virtual.ua/images/374585/akvapark-lviv.virtual.ua_002.jpg',
                            place_id=place17.id)
    photo_17_3 = PlacePhoto(image='https://ua.igotoworld.com/frontend/webcontent/websites/1/images/'
                                  'gallery/10731_800x600_LvivAkvapark02.jpg', place_id=place17.id)
    photo_17_4 = PlacePhoto(image='https://akvapark-lviv.virtual.ua/images/374595/akvapark-lviv.virtual.ua_009.jpg',
                            place_id=place17.id)
    photo_17_5 = PlacePhoto(image='https://www.nezabarom.ua/img/objects/bce9a8251b.jpg', place_id=place17.id)

    photo_18_1 = PlacePhoto(image='https://i.pinimg.com/236x/2d/c8/a9/2dc8a9c5028458d1e62ede009f5f0979.jpg',
                            place_id=place18.id)
    photo_18_2 = PlacePhoto(image='https://i.pinimg.com/236x/39/79/87/397987ba15cd44b9f4f5b1bb72ec6341.jpg',
                            place_id=place18.id)
    photo_18_3 = PlacePhoto(image='https://i.pinimg.com/236x/4a/9d/34/4a9d3464a9e2806cdc9dff4135a806ef.jpg',
                            place_id=place18.id)
    photo_18_4 = PlacePhoto(image='https://i.pinimg.com/236x/1b/a6/bc/1ba6bc72e5bbb40b1816585f781f0608.jpg',
                            place_id=place18.id)
    photo_18_5 = PlacePhoto(image='https://i.pinimg.com/236x/c0/a8/bd/c0a8bd75f77b854e4da640976c323756.jpg',
                            place_id=place18.id)

    photo_19_1 = PlacePhoto(image='https://kufer.media/wp-content/uploads/2019/12/'
                                  'alexandra-luniel-03Hz0iuig8c-unsplash-1.jpg', place_id=place19.id)
    photo_19_2 = PlacePhoto(image='https://vsitury.com.ua/uploads/224/72635/2.jpg', place_id=place19.id)
    photo_19_3 = PlacePhoto(image='https://karpatium.com.ua/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6Ik'
                                  'JBaHBBbUVDIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--fe24cce9dcf888a20d4966de7560e71'
                                  'e35be5ae5/mt_homiak.jpeg', place_id=place19.id)
    photo_19_4 = PlacePhoto(image='https://i.pinimg.com/originals/5f/1d/47/5f1d474b4fee059331f6e4cf79752aba.jpg',
                            place_id=place19.id)
    photo_19_5 = PlacePhoto(image='https://calendar.karpaty.ua/uploads/article_photos/1467902189-328778__3.jpg',
                            place_id=place19.id)
    # 'https://faynotour.com/wp-content/uploads/2021/07/homjak-3.jpg'
    # 'https://guide.karpaty.ua/uploads/article_photos/w420_1458144950-804682__w420_chomyak4.jpg'

    photo_20_1 = PlacePhoto(image='https://travelland.com.ua/wp-content/uploads/2019/05/2018-05-03_232822.jpg',
                            place_id=place20.id)
    photo_20_2 = PlacePhoto(image='https://svitkarpat.org/wp-content/uploads/2020/05/Hora-Makovytsia-YAremche.jpg',
                            place_id=place20.id)
    photo_20_3 = PlacePhoto(image='https://pershij.com.ua/wp-content/uploads/2018/04/2407.jpg', place_id=place20.id)
    photo_20_4 = PlacePhoto(image='https://ua.igotoworld.com/frontend/webcontent/websites/1/images/'
                                  'gallery/69606_370x246_Magura_(Jablunycia).jpg', place_id=place20.id)
    photo_20_5 = PlacePhoto(image='https://vpohid.com.ua/static/photothumbs/2606_1000.jpg', place_id=place20.id)

    photo_21_1 = PlacePhoto(image='https://2.bp.blogspot.com/-jGg3-B8830k/WDBG7fdR1cI/AAAAAAAAJ1E/'
                                  'HGrgEYuZjdYAMWw4ciuyjiK0mDf6b1KHwCLcB/s640/DSC_0552-1.jpg', place_id=place21.id)
    photo_21_2 = PlacePhoto(image='https://4.bp.blogspot.com/-S6qGfVGfpDg/WDBHL4qJIpI/AAAAAAAAJ1g/'
                                  'rYLpwOc_WbICe9BClzHkSqq3AFbxpXqHQCLcB/s640/DSC_0572-1.jpg', place_id=place21.id)
    photo_21_3 = PlacePhoto(image='https://3.bp.blogspot.com/-2QrqndPd0oM/WDBHjMcfsEI/AAAAAAAAJ2I/'
                                  '1tjejRtq-0cgNql9TfaGBwtZOeVr5L6YwCLcB/s640/DSC_0598-1.jpg', place_id=place21.id)
    photo_21_4 = PlacePhoto(image='https://karpatium.com.ua/rails/active_storage/representations/eyJfcmFpbHMiOnsibWVz'
                                  'c2FnZSI6IkJBaHBBdnNGIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--2aeac10b222264c8235f'
                                  '3a56328d81db8619af24/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCam9MY21WemFYcGxTU0lKTkRVd'
                                  '2VBWTZCa1ZVIiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--83112b0b002f5b4ddfaaafb9c'
                                  'db3a656043aef2a/%D0%BA%D0%BE%D0%BB%D0%B8%D0%B1%D0%B0-%D0%B3%D0%BE%D1%80%D0%B0-%D1%'
                                  '8F%D0%B3%D1%96%D0%B4%D0%BD%D0%B0.jpeg', place_id=place21.id)
    photo_21_5 = PlacePhoto(image='https://proydisvit.com/userfiles/131342738_668714507151043_917174649037638497_n.jpg',
                            place_id=place21.id)

    photo_22_1 = PlacePhoto(image='https://travels-ukraine.com/wp-content/uploads/2017/03/IMG_5133.jpg',
                            place_id=place22.id)
    photo_22_2 = PlacePhoto(image='https://travels-ukraine.com/wp-content/uploads/2017/03/4-marshrut-na-parashku.jpg',
                            place_id=place22.id)
    photo_22_3 = PlacePhoto(image='https://find-way.com.ua/components/com_jshopping/files/img_products/'
                                  'full_GOPR6314.jpg', place_id=place22.id)
    photo_22_4 = PlacePhoto(image='https://stezhkamu.com/img/places/473/2681.jpg', place_id=place22.id)
    photo_22_5 = PlacePhoto(image='https://stezhkamu.com/img/places/473/2685.jpg', place_id=place22.id)

    photo_23_1 = PlacePhoto(image='https://i.ytimg.com/vi/ZCt799iZO78/maxresdefault.jpg',
                            place_id=place23.id)
    photo_23_2 = PlacePhoto(image='https://travels-ukraine.com/wp-content/uploads/2016/11/61512_800x600_bukovel3-2.jpg',
                            place_id=place23.id)
    photo_23_3 = PlacePhoto(image='https://i.ytimg.com/vi/pjkhZxwc_po/maxresdefault.jpg', place_id=place23.id)
    photo_23_4 = PlacePhoto(image='https://i.ytimg.com/vi/lm2lQHMf6G4/maxresdefault.jpg', place_id=place23.id)
    photo_23_5 = PlacePhoto(image='https://static.rootsrated.com/image/upload/s--P9UQL-z0--/'
                                  't_rr_large_traditional/hfn5r7y4gkheon31gpcu.jpg', place_id=place23.id)

    photo_24_1 = PlacePhoto(image='https://i.ytimg.com/vi/xxRUAW93nKE/maxresdefault.jpg', place_id=place24.id)
    photo_24_2 = PlacePhoto(image='https://i.ytimg.com/vi/lm2lQHMf6G4/maxresdefault.jpg', place_id=place24.id)
    photo_24_3 = PlacePhoto(image='https://content.26in.fr/p/pictures/4/9/7/49725/1d9d1c-9.jpg',
                            place_id=place24.id)
    photo_24_4 = PlacePhoto(image='https://u.profitroom.com/2018-czarnaperla-czarnagora-pl/thumb/1840x840/uploads/'
                                  'test/IMG_2995_CzarnaGora_ABC_Staronphoto.jpg', place_id=place24.id)
    photo_24_5 = PlacePhoto(image='https://content.26in.fr/p/pictures/3/5/5/35534/39d016-9.jpg', place_id=place24.id)

    photo_25_1 = PlacePhoto(image='https://i.ytimg.com/vi/lm2lQHMf6G4/maxresdefault.jpg', place_id=place25.id)
    photo_25_2 = PlacePhoto(image='https://keyassets.timeincuk.net/inspirewp/live/wp-content/uploads/sites/'
                                  '11/2014/09/ISAC6425.jpg', place_id=place25.id)
    photo_25_3 = PlacePhoto(image='https://i.ytimg.com/vi/xxRUAW93nKE/maxresdefault.jpg', place_id=place25.id)
    photo_25_4 = PlacePhoto(image='https://minttours.com/wp-content/uploads/2020/05/Canada_Whistler-Bike-Park_14.jpg',
                            place_id=place25.id)
    photo_25_5 = PlacePhoto(image='https://www.moredirt.com/photos/90578.jpg', place_id=place25.id)

    photo_26_1 = PlacePhoto(image='https://i.ytimg.com/vi/lX8lv0Q4GyQ/maxresdefault.jpg', place_id=place26.id)
    photo_26_2 = PlacePhoto(image='https://verkhovyna.life/files_ci/168/verkhovynalife-cheremosh1__large.jpg',
                            place_id=place26.id)
    photo_26_3 = PlacePhoto(image='https://skyta.com.ua/trash/statica/0/f76a65b24818f95a2525ba0be8729865_600x1000.jpg',
                            place_id=place26.id)
    photo_26_4 = PlacePhoto(image='https://i.tyzhden.ua/content/photoalbum/2016/07_2016/04/river/05.jpg',
                            place_id=place26.id)
    photo_26_5 = PlacePhoto(image='https://i.ytimg.com/vi/YTnTAmbPvIk/maxresdefault.jpg', place_id=place26.id)

    photo_27_1 = PlacePhoto(image='https://internet-bilet.ua/images/room_header_photo/size3/'
                                  'hph_1487841574_58aea9265efed.jpg', place_id=place27.id)
    photo_27_2 = PlacePhoto(image='https://upload.wikimedia.org/wikipedia/uk/1/12/Velotrack_ska.jpg',
                            place_id=place27.id)
    photo_27_3 = PlacePhoto(image='https://tvoemisto.tv/media/gallery/full/1/2/1247984_o.jpg', place_id=place27.id)
    photo_27_4 = PlacePhoto(image='https://f.mixsport.pro/location/9335/0nbIE.jpg', place_id=place27.id)

    db.session.add_all([photo_1_1, photo_1_2, photo_1_3, photo_1_4, photo_1_5,
                        photo_2_1, photo_2_2, photo_2_3, photo_2_4, photo_2_5,
                        photo_3_1, photo_3_2, photo_3_3, photo_3_4, photo_3_5,
                        photo_4_1, photo_4_2, photo_4_3, photo_4_4, photo_4_5,
                        photo_5_1, photo_5_2, photo_5_3, photo_5_4, photo_5_5,
                        photo_6_1, photo_6_2, photo_6_3, photo_6_4, photo_6_5,
                        photo_7_1, photo_7_2, photo_7_3, photo_7_4, photo_7_5,
                        photo_8_1, photo_8_2, photo_8_3, photo_8_4, photo_8_5,
                        photo_9_1, photo_9_2, photo_9_3, photo_9_4, photo_9_5,
                        photo_10_1, photo_10_2, photo_10_3, photo_10_4, photo_10_5,
                        photo_11_1, photo_11_2, photo_11_3, photo_11_4, photo_11_5,
                        photo_12_1, photo_12_2, photo_12_3, photo_12_4, photo_12_5,
                        photo_13_1, photo_13_2, photo_13_3, photo_13_4, photo_13_5,
                        photo_14_1, photo_14_2, photo_14_3, photo_14_4, photo_14_5,
                        photo_15_1, photo_15_2, photo_15_3, photo_15_4, photo_15_5,
                        photo_16_1, photo_16_2, photo_16_3, photo_16_4, photo_16_5,
                        photo_17_1, photo_17_2, photo_17_3, photo_17_4, photo_17_5,
                        photo_18_1, photo_18_2, photo_18_3, photo_18_4, photo_18_5,
                        photo_19_1, photo_19_2, photo_19_3, photo_19_4, photo_19_5,
                        photo_20_1, photo_20_2, photo_20_3, photo_20_4, photo_20_5,
                        photo_21_1, photo_21_2, photo_21_3, photo_21_4, photo_21_5,
                        photo_22_1, photo_22_2, photo_22_3, photo_22_4, photo_22_5,
                        photo_23_1, photo_23_2, photo_23_3, photo_23_4, photo_23_5,
                        photo_24_1, photo_24_2, photo_24_3, photo_24_4, photo_24_5,
                        photo_25_1, photo_25_2, photo_25_3, photo_25_4, photo_25_5,
                        photo_26_1, photo_26_2, photo_26_3, photo_26_4, photo_26_5,
                        photo_27_1, photo_27_2, photo_27_3, photo_27_4
                        ])
    db.session.commit()
