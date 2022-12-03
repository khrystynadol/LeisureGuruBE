from models import app, db, Place, Season, Activity, PlaceActivity, PlaceSeason  # , User

with app.app_context():

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
    activity7 = Activity(name="Eating")
    db.session.add_all([season1, season2, season3, season4,
                        activity1, activity2, activity3, activity4, activity5,
                        activity6, activity7])
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

    db.session.add_all([place1, place2, place3, place4, place5,
                        place6, place7, place8, place9, place10,
                        place11, place12, place13, place14, place15])
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
                        place_activity11, place_activity12, place_activity13, place_activity14, place_activity15])
    db.session.commit()
