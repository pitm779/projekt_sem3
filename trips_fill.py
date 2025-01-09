import pymysql

conn = pymysql.connect(
    host='giniewicz.it',
    user='team03',
    password='te@mzaoe',
    db='team03',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # table reset 
        sql_delete = "DELETE FROM `trips`"
        sql_reset_index = "ALTER TABLE `trips` AUTO_INCREMENT = 1"
        cursor.execute(sql_delete)
        conn.commit()
        cursor.execute(sql_reset_index)
        conn.commit()

        nazwy = [
                ['Trekking na Kilimandżaro', 1, 'Wyrusz na przygodę życia i zdobądź najwyższy szczyt Afryki! Kilimandżaro oferuje niezwykłą podróż przez tropikalne lasy, surowe wrzosowiska i lodowe krajobrazy. To wyzwanie nie tylko fizyczne, ale i duchowe – każdy krok przybliża Cię do spektakularnego widoku z Uhuru Peak (5895 m n.p.m.). W otoczeniu afrykańskiej przyrody, z pomocą doświadczonych przewodników, odkryjesz, że Twoje możliwości są większe, niż kiedykolwiek myślałeś.', True],
                ['Polowanie na Zorzę Polarną w Arktyce', 1, 'Wyrusz na niezapomnianą wyprawę za koło podbiegunowe i stań twarzą w twarz z jednym z najpiękniejszych zjawisk natury – zorzą polarną. W mroźnym pięknie arktycznego krajobrazu, otoczony ciszą i majestatem natury, czeka Cię noc pełna magii. Z pomocą lokalnych przewodników i najskuteczniejszych wskazówek zwiększysz szanse na ujrzenie migoczących świateł na niebie. Po drodze czekają na Ciebie kuligi psimi zaprzęgami, zorbing na lodzie i niesamowite widoki śnieżnych pustkowi.', True],
                ['Podwodne Odkrycia w Wielkiej Rafie Koralowej', 1, 'Zanurz się w krystalicznych wodach Australii i odkryj cuda Wielkiej Rafy Koralowej – największego podwodnego ekosystemu na Ziemi! Wśród kolorowych koralowców, egzotycznych ryb i tajemniczych morskich stworzeń czeka Cię przygoda jak z filmu przyrodniczego. Snorkeling, nurkowanie czy rejs łodzią ze szklanym dnem – wybierz swój sposób na eksplorację tego naturalnego cudu. Każdy dzień to nowe odkrycia i niezapomniane widoki, które na zawsze pozostaną w Twojej pamięci.', True],
                ['Tajemnicze Zakątki Machu Picchu', 2, 'Odkryj magiczne Machu Picchu – zaginione miasto Inków skryte w chmurach peruwiańskich Andów. Przejdź ścieżkami, którymi kiedyś kroczyli dawni władcy, i podziwiaj niezwykłe tarasy, świątynie i widoki, które zapierają dech w piersiach. Każdy zakątek tego starożytnego kompleksu kryje w sobie historię, legendy i tajemnice czekające na odkrycie. Z pomocą lokalnych przewodników zanurzysz się w kulturze i duchowości Inków, jednocześnie ciesząc się pięknem otaczających krajobrazów.', True],
                ['Podróż w Czasie - Odkrywanie Pompejów', 2, 'Przenieś się do czasów starożytnego Rzymu i odkryj Pompeje – miasto zatrzymane w czasie przez erupcję Wezuwiusza. Spaceruj po ulicach, gdzie przed wiekami tętniło życie, podziwiaj doskonale zachowane mozaiki, freski i rzymską architekturę. Z pomocą przewodnika poznasz historie mieszkańców, ich codzienne zwyczaje i tragiczne losy. Każdy krok w tym wyjątkowym miejscu pozwala poczuć atmosferę antycznej epoki i zrozumieć potęgę natury.', True],
                ['Gotyckie Zamki Dolnego Śląska', 2, 'Odkryj majestatyczne gotyckie zamki Dolnego Śląska – pełne tajemnic, legend i średniowiecznego uroku. Od zamku Książ, pełnego bogactw i intryg, po Zamek Czocha, skrywający sekrety przeszłości, każdy z nich przeniesie Cię do czasów rycerzy, dam dworu i królów. Spaceruj po tajemnych korytarzach, podziwiaj monumentalne wieże i chłód kamiennych sal. Poznaj historie o duchach, ukrytych skarbach i niezwykłych wydarzeniach, które nadają temu regionowi wyjątkowy klimat.', False],
                ['Kosmiczna Przygoda w Centrum NASA na Florydzie', 3, 'Wyrusz w fascynującą podróż w kosmos, nie opuszczając Ziemi! Centrum NASA na Florydzie to miejsce, gdzie technologia spotyka się z marzeniami o gwiazdach. Zobacz potężne rakiety, poczuj dreszcz symulowanego startu i poznaj kulisy misji kosmicznych, które zmieniły historię ludzkości. To interaktywne doświadczenie przeniesie Cię w świat astronautów, nieskończonego wszechświata i przyszłości eksploracji kosmosu.', True],
                ['Dziecięcy Raj w Parku Rozrywki Energylandia', 3, 'Przygotuj się na dzień pełen emocji i radości w największym parku rozrywki w Polsce! Energylandia to ponad 100 atrakcji dla całej rodziny – od strefy malucha po ekstremalne rollercoastery, które przyprawią Cię o zawrót głowy. Bajkowe dekoracje, wodne przygody i widowiskowe pokazy sprawią, że każde dziecko (i dorosły) poczuje się jak w magicznym świecie. ', False],
                ['Jurassic Park Live: Dinozaury w Realnym Świecie', 3, 'Przenieś się miliony lat wstecz i spotkaj gigantyczne dinozaury w pełnej skali! Park Jurassic Live to miejsce, gdzie nauka spotyka się z przygodą – realistyczne modele prehistorycznych gadów, interaktywne wystawy i symulacje pozwolą Ci poczuć, jak wyglądało życie w erze mezozoicznej. Spaceruj pośród gigantów, poznaj tajemnice ich przetrwania i zobacz, jak naukowcy ożywiają historię.', True],
                ['Transcendentalne Warsztaty Jogi w Himalajach', 4, 'Zanurz się w duchowej harmonii i odkryj wewnętrzny spokój w sercu najwyższych gór świata. Warsztaty jogi w Himalajach to wyjątkowe doświadczenie, które łączy głęboką medytację, praktykę oddechową i wędrówki po mistycznych szlakach. W otoczeniu majestatycznych szczytów, pod okiem mistrzów, nauczysz się sztuki równowagi ciała i umysłu. To podróż do samego siebie, gdzie piękno natury inspiruje do odnalezienia własnej siły i spokoju.', True],
                ['Sanktuarium na Jasnej Górze - Duchowe Oczyszczenie', 4, 'Pielgrzymka na Jasną Górę to wyjątkowa okazja do wzmocnienia wiary i odnalezienia duchowego spokoju. W otoczeniu historycznego klasztoru i Cudownego Obrazu Matki Boskiej Częstochowskiej poczujesz głębokie połączenie z duchowością. Modlitwa, chwile refleksji i zwiedzanie tego niezwykłego miejsca oferują ciszę i ukojenie dla duszy. To podróż, która odnowi Twojego ducha i przyniesie wewnętrzną harmonię.', False],
                ['Rytuał w szamańskiej wiosce w Peru', 4, 'Wyrusz w duchową podróż do serca peruwiańskiej Amazonii, gdzie czeka na Ciebie niezwykły rytuał ayahuaski prowadzony przez lokalnych szamanów. To mistyczne doświadczenie oczyszczania ciała i umysłu pozwala spojrzeć głęboko w siebie, zyskać nową perspektywę i połączyć się z naturą. Przy dźwiękach tradycyjnych pieśni i w otoczeniu dzikiej dżungli odkryjesz dawne rytuały, które łączą ludzi z duchowym światem. To podróż, która zmienia na zawsze.', True],
                ['Surfing na Plażach Australii - Wyspy Byrona', 5, 'Poczuj adrenalinę i złap idealną falę na rajskich plażach Byron Bay! To miejsce, gdzie ocean spotyka się z przygodą, oferując doskonałe warunki do surfingu dla początkujących i zaawansowanych. Zanurz się w surferskim stylu życia, podziwiaj zachody słońca nad Pacyfikiem i ciesz się luźną atmosferą australijskiego wybrzeża.', True],
                ['Wspinaczka na Ścianę Trolla w Norwegii', 5, 'Zmierz się z jedną z najbardziej spektakularnych formacji skalnych w Europie – legendarną Ścianą Trolla! Ta monumentalna ściana wznosi się na wysokość 1100 metrów i stanowi wyzwanie dla wspinaczy z całego świata. Z pomocą profesjonalnych przewodników pokonasz naturalne bariery, podziwiając zapierające dech w piersiach krajobrazy norweskich fiordów.', True],
                ['Rowerem przez Holandię - Szlaki Tulipanów', 5, 'Przemierzaj malownicze holenderskie krajobrazy na rowerze, mijając pola tulipanów w pełnym rozkwicie, urokliwe wiatraki i kanały. Szlaki tulipanowe to esencja wiosennej Holandii, idealna dla każdego, kto chce połączyć aktywny wypoczynek z kontemplacją piękna natury.', True],
                ['Koncerty w Operze Wiedeńskiej', 6, 'Wejdź do jednej z najpiękniejszych sal koncertowych świata i zanurz się w dźwiękach muzyki klasycznej na żywo. Opera Wiedeńska to miejsce, gdzie historia i kultura spotykają się z perfekcją artystyczną. Zasiądź w eleganckim wnętrzu i pozwól, by dźwięki Mozarta, Beethovena czy Straussa przeniosły Cię w inny wymiar. '], True,
                ['Karnawał w Rio de Janeiro', 6, 'Poczuj niesamowitą atmosferę najsłynniejszego karnawału na świecie! Rio de Janeiro eksploduje kolorami, dźwiękami samby i radością życia podczas tej wyjątkowej imprezy. Uliczne parady, widowiskowe kostiumy i gorące rytmy tworzą spektakl, który zapiera dech w piersiach. To święto, które trzeba przeżyć na własnej skórze, by zrozumieć jego magię!', True],
                ['Karnawał w Wenecji', 6, 'Weź udział w najpiękniejszym i najbardziej eleganckim karnawale Europy! Wenecja zamienia się w scenę pełną bogato zdobionych masek, historycznych kostiumów i tajemniczych balów. Przemierzaj wąskie uliczki i kanały, podziwiając niezwykłą atmosferę miasta, które staje się żywym muzeum renesansu. ', True]
        ]
        #karnawaly odbywaja sie w konkretynych porach roku (okresach roku), podczas generowania dat prosze pamietajcie o tym
        for x in nazwy:
        # Create a new record
            sql = "INSERT INTO `trips` (`trip_name`, `category_id`, `description`, `abroad`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (x[0], x[1],x[2], x[3]))

            conn.commit()

        # Read data from database
        # sql = "SELECT * FROM `trip_category`"
        # cursor.execute(sql)

        # Fetch all rows
        # rows = cursor.fetchall()

        # Print results
        # for row in rows:
            # print(row)
finally:
    conn.close()

