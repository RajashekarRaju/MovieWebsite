import media
import fresh_tomatoes

captain_america = media.Movie("Captain America: The First Avenger",
                              "Predominantly set during World War II, Steve Rogers is a sickly man from Brooklyn "
                              "who's transformed into super-soldier Captain America to aid in the war effort. Rogers "
                              "must stop the Red Skull – Adolf Hitler's ruthless head of weaponry, and the leader of "
                              "an organization that intends to use a mysterious device of untold powers for world "
                              "domination.",
                              "http://www.movienewsletters.net/photos/277218R1.jpg",
                              "https://www.youtube.com/watch?v=JerVrbLldXw")

the_avengers = media.Movie("The avengers",
                           "When an unexpected enemy emerges and threatens global safety and security, Nick Fury, "
                           "director of the international peacekeeping agency known as S.H.I.E.L.D., finds himself in "
                           "need of a team to pull the world back from the brink of disaster. Spanning the globe, "
                           "a daring recruitment effort begins!",
                           "http://www.movienewsletters.net/photos/130835R1.jpg",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

doctor_strange = media.Movie("Doctor strange",
                             "After his career is destroyed, a brilliant but arrogant surgeon gets a new lease on "
                             "life when a sorcerer takes him under her wing and trains him to defend the world "
                             "against evil.",
                             "https://contentserver.com.au/assets/491602_p11214341_p_v8_ap.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM")

thor_ragnorok = media.Movie("Thor: Ragnarok",
                            "Thor is on the other side of the universe and finds himself in a race against time to "
                            "get back to Asgard to stop Ragnarok, the prophecy of destruction to his homeworld and "
                            "the end of Asgardian civilization, at the hands of an all-powerful new threat, "
                            "the ruthless Hela.",
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                            "https://www.youtube.com/watch?v=ue80QwXMRHg")

iron_man_3 = media.Movie("Iron Man 3",
                         "When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, "
                         "he starts an odyssey of rebuilding and retribution.",
                         "https://terrigen-cdn-dev.marvel.com/content/prod/1x/ironman3_lob_crd_01_10.jpg",
                         "https://www.youtube.com/watch?v=YLorLVa95Xo")

the_hulk = media.Movie("The Incredible Hulk",
                       "Scientist Bruce Banner scours the planet for an antidote to the unbridled force of rage "
                       "within him: the Hulk. But when the military masterminds who dream of exploiting his powers "
                       "force him back to civilization, he finds himself coming face to face with a new, deadly foe.",
                       "http://www.movienewsletters.net/photos/277217R1.jpg",
                       "https://www.youtube.com/watch?v=xbqNb2PFKKA")

movies = [doctor_strange, thor_ragnorok, iron_man_3, the_hulk, captain_america, the_avengers]
fresh_tomatoes.open_movies_page(movies)
