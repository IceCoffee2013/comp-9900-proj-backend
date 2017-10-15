import json
import re


street_type = {'road', 'street', 'avenue', 'tunnel', 'lane', 'bridge', 'highway', 'parade'}

suburbs = ['Abbotsbury', 'Abbotsford', 'Acacia Gardens', 'Agnes Banks', 'Airds', 'Alexandria', 'Alfords Point',
           'Allambie Heights', 'Allawah', 'Ambarvale', 'Annandale', 'Annangrove', 'Arcadia', 'Arncliffe',
           'Arndell Park', 'Artarmon', 'Ashbury', 'Ashcroft', 'Ashfield', 'Asquith', 'Auburn', 'Austral',
           'Avalon Beach'] \
          + ['Badgerys Creek', 'Balgowlah', 'Balgowlah Heights', 'Balmain', 'Balmain East', 'Bangor',
             'Banksia', 'Banksmeadow', 'Bankstown', 'Bankstown Aerodrome', 'Barangaroo',
             'Barden Ridge', 'Bardia', 'Bardwell Park', 'Bardwell Valley', 'Barra Brui', 'Bass Hill',
             'Baulkham Hills', 'Bayview', 'Beacon Hill', 'Beaconsfield', 'Beaumont Hills', 'Beecroft',
             'Belfield', 'Bella Vista', 'Bellevue Hill', 'Belmore', 'Belrose', 'Berala',
             'Berkshire Park', 'Berowra', 'Berowra Creek', 'Berowra Heights', 'Berowra Waters',
             'Berrilee', 'Beverley Park', 'Beverly Hills', 'Bexley', 'Bexley North', 'Bickley Vale',
             'Bidwill', 'Bilgola Beach', 'Bilgola Plateau', 'Birchgrove', 'Birrong', 'Blackett',
             'Blacktown', 'Blair Athol', 'Blairmount', 'Blakehurst', 'Bligh Park', 'Bondi',
             'Bondi Beach', 'Bondi Junction', 'Bonnet Bay', 'Bonnyrigg', 'Bonnyrigg Heights',
             'Bossley Park', 'Botany', 'Bow Bowing', 'Box Hill', 'Bradbury', 'Breakfast Point',
             'Brighton-Le-Sands', 'Bringelly', 'Bronte', 'Brooklyn', 'Brookvale', 'Bundeena',
             'Bungarribee', 'Burwood', 'Burwood Heights', 'Busby'] \
          + ['Cabarita', 'Cabramatta', 'Cabramatta West', 'Caddens', 'Cambridge Gardens', 'Cambridge Park', 'Camden',
             'Camden South', 'Camellia', 'Cammeray', 'Campbelltown', 'Camperdown', 'Campsie', 'Canada Bay',
             'Canley Heights', 'Canley Vale', 'Canoelands', 'Canterbury', 'Caringbah', 'Caringbah South', 'Carlingford',
             'Carlton', 'Carnes Hill', 'Carramar', 'Carss Park', 'Cartwright', 'Castle Cove', 'Castle Hill',
             'Castlecrag', 'Castlereagh', 'Casula', 'Catherine Field', 'Cattai', 'Cawdor', 'Cecil Hills', 'Cecil Park',
             'Centennial Park', 'Central Business District', 'Chatswood', 'Chatswood West', 'Cheltenham', 'Cherrybrook',
             'Chester Hill', 'Chifley', 'Chippendale', 'Chipping Norton', 'Chiswick', 'Chullora', 'Church Point',
             'Claremont Meadows', 'Clarendon', 'Clareville', 'Claymore', 'Clemton Park', 'Clontarf', 'Clovelly',
             'Clyde', 'Coasters Retreat', 'Cobbitty', 'Colebee', 'Collaroy', 'Collaroy Plateau', 'Colyton', 'Como',
             'Concord', 'Concord West', 'Condell Park', 'Connells Point', 'Constitution Hill', 'Coogee',
             'Cottage Point', 'Cowan', 'Cranebrook', 'Cremorne', 'Cremorne Point', 'Cromer', 'Cronulla', 'Crows Nest',
             'Croydon', 'Croydon Park', 'Curl Curl', 'Currans Hill', 'Currawong Beach'] \
          + ['Daceyville', 'Dangar Island', 'Darling Point', 'Darlinghurst', 'Darlington', 'Davidson', 'Dawes Point',
             'Dean Park', 'Dee Why', 'Denham Court', 'Denistone', 'Denistone East', 'Denistone West', 'Dharruk',
             'Dolans Bay', 'Dolls Point', 'Doonside', 'Double Bay', 'Dover Heights', 'Drummoyne', 'Duffys Forest',
             'Dulwich Hill', 'Dundas', 'Dundas Valley', 'Dural'] \
          + ['Eagle Vale', 'Earlwood', 'East Gordon', 'East Hills', 'East Killara', 'East Lindfield', 'East Ryde',
             'East Sydney', 'Eastern Creek', 'Eastgardens', 'Eastlakes', 'Eastwood', 'Edensor Park', 'Edgecliff',
             'Edmondson Park', 'Elanora Heights', 'Elderslie', 'Elizabeth Bay', 'Elizabeth Hills', 'Ellis Lane',
             'Elvina Bay', 'Emerton', 'Emu Heights', 'Emu Plains', 'Enfield', 'Engadine', 'Englorie Park', 'Enmore',
             'Epping', 'Ermington', 'Erskine Park', 'Erskineville', 'Eschol Park', 'Eveleigh'] \
          + ['Fairfield', 'Fairfield East', 'Fairfield Heights', 'Fairfield West', 'Fairlight', 'Fiddletown',
             'Five Dock', 'Flemington', 'Forest Glen', 'Forest Lodge', 'Forestville', 'Freemans Reach',
             'Frenchs Forest', 'Freshwater'] \
          + ['Galston', 'Georges Hall', 'Gilead', 'Girraween', 'Gladesville', 'Glebe', 'Gledswood Hills', 'Glen Alpine',
             'Glendenning', 'Glenfield', 'Glenhaven', 'Glenmore Park', 'Glenorie', 'Glenwood', 'Glossodia', 'Gordon',
             'Granville', 'Grasmere', 'Grays Point', 'Great Mackerel Beach', 'Green Valley', 'Greenacre', 'Greendale',
             'Greenfield Park', 'Greenhills Beach', 'Greenwich', 'Gregory Hills', 'Greystanes', 'Guildford',
             'Guildford West', 'Gymea', 'Gymea Bay'] \
          + ['Haberfield', 'Hammondville', 'Harrington Park', 'Harris Park', 'Hassall Grove', 'Hawkesbury River',
             'Haymarket', 'Heathcote', 'Hebersham', 'Heckenberg', 'Henley', 'Hillsdale', 'Hinchinbrook', 'Hobartville',
             'Holroyd', 'Holsworthy', 'Homebush', 'Homebush West', 'Horningsea Park', 'Hornsby', 'Hornsby Heights',
             'Horsley Park', 'Hoxton Park', 'Hunters Hill', 'Huntingwood', 'Huntleys Cove', 'Huntleys Point',
             'Hurlstone Park', 'Hurstville', 'Hurstville Grove'] \
          + ['Illawong', 'Ingleburn', 'Ingleside'] \
          + ['Jamisontown', 'Jannali', 'Jordan Springs'] \
          + ['Kangaroo Point', 'Kareela', 'Kearns', 'Kellyville', 'Kellyville Ridge', 'Kemps Creek', 'Kensington',
             'Kenthurst', 'Kentlyn', 'Killara', 'Killarney Heights', 'Kings Cross', 'Kings Langley', 'Kings Park',
             'Kingsford', 'Kingsgrove', 'Kingswood', 'Kingswood Park', 'Kirkham', 'Kirrawee', 'Kirribilli', 'Kogarah',
             'Kogarah Bay', 'Ku-ring-gai Chase', 'Kurnell', 'Kurraba Point', 'Kyeemagh', 'Kyle Bay'] \
          + ['La Perouse', 'Lakemba', 'Lalor Park', 'Lane Cove', 'Lane Cove North', 'Lane Cove West', 'Lansdowne',
             'Lansvale', 'Laughtondale', 'Lavender Bay', 'Leets Vale', 'Leichhardt', 'Len Waters Estate', 'Leonay',
             'Leppington', 'Lethbridge Park', 'Leumeah', 'Lewisham', 'Liberty Grove', 'Lidcombe', 'Lilli Pilli',
             'Lilyfield', 'Lindfield', 'Linley Point', 'Little Bay', 'Liverpool', 'Llandilo', 'Loftus', 'Londonderry',
             'Long Point', 'Longueville', 'Lower Portland', 'Luddenham', 'Lugarno', 'Lurnea'] \
          + ['Macquarie Fields', 'Macquarie Links', 'Macquarie Park', 'Maianbar', 'Malabar', 'Manly', 'Manly Vale',
             'Maraylya', 'Marayong', 'Maroota', 'Maroubra', 'Marrickville', 'Marsden Park', 'Marsfield', 'Mascot',
             'Matraville', 'Mays Hill', 'McCarrs Creek', 'McGraths Hill', 'McMahons Point', 'Meadowbank',
             'Melrose Park', 'Menai', 'Menangle Park', 'Merrylands', 'Merrylands West', 'Middle Cove', 'Middle Dural',
             'Middleton Grange', 'Miller', 'Millers Point', 'Milperra', 'Milsons Passage', 'Milsons Point',
             'Minchinbury', 'Minto', 'Minto Heights', 'Miranda', 'Mona Vale', 'Monterey', 'Moore Park', 'Moorebank',
             'Mortdale', 'Mortlake', 'Mosman', 'Mount Annan', 'Mount Colah', 'Mount Druitt', 'Mount Kuring-Gai',
             'Mount Lewis', 'Mount Pritchard', 'Mount Vernon', 'Mulgoa', 'Mulgrave'] \
          + ['Narellan Vale', 'Naremburn', 'Narrabeen', 'Narraweena', 'Narwee', 'Nelson', 'Neutral Bay', 'Newington',
             'Newport', 'Newtown', 'Normanhurst', 'North Balgowlah', 'North Bondi', 'North Curl Curl', 'North Epping',
             'North Manly', 'North Narrabeen', 'North Parramatta', 'North Richmond', 'North Rocks', 'North Ryde',
             'North Seaforth', 'North St Ives', 'North St Marys', 'North Strathfield', 'North Sydney',
             'North Turramurra', 'North Willoughby', 'North Wahroonga', 'Northbridge', 'Northmead', 'Northwood'] \
          + ['Oakhurst', 'Oakville', 'Oatlands', 'Oatley', 'Old Guildford', 'Old Toongabbie', 'Oran Park',
             'Orchard Hills', 'Osborne Park', 'Oxford Falls', 'Oxley Park', 'Oyster Bay'] \
          + ['Paddington', 'Padstow', 'Padstow Heights', 'Pagewood', 'Palm Beach', 'Panania', 'Parklea', 'Parramatta',
             'Peakhurst', 'Peakhurst Heights', 'Pemulwuy', 'Pendle Hill', 'Pennant Hills', 'Penrith', 'Penshurst',
             'Petersham', 'Phillip Bay', 'Picnic Point', 'Pitt Town', 'Pleasure Point', 'Plumpton', 'Point Piper',
             'Port Botany', 'Potts Hill', 'Potts Point', 'Prairiewood', 'Prestons', 'Punchbowl', 'Putney',
             'Pymble', 'Pyrmont'] \
          + ['Quakers Hill', 'Queens Park', 'Queenscliff'] \
          + ['Raby', 'Ramsgate', 'Ramsgate Beach', 'Randwick', 'Redfern', 'Regents Park', 'Regentville', 'Revesby',
             'Revesby Heights', 'Rhodes', 'Richmond', 'Riverstone', 'Riverview', 'Riverwood', 'Rockdale', 'Rodd Point',
             'Rookwood', 'Rooty Hill', 'Ropes Crossing', 'Rose Bay', 'Rosebery', 'Rosehill', 'Roselands', 'Rosemeadow',
             'Roseville', 'Roseville Chase', 'Rouse Hill', 'Royal National Park', 'Rozelle', 'Ruse', 'Rushcutters Bay',
             'Russell Lea', 'Rydalmere', 'Ryde'] \
          + ['Sackville North', 'Sadleir', 'Sandringham', 'Sans Souci', 'Scheyville', 'Schofields', 'Scotland Island',
             'Seaforth', 'Sefton', 'Seven Hills', 'Shalvey', 'Shanes Park', 'Silverwater', 'Singletons Mill',
             'Smeaton Grange', 'Smithfield', 'South Coogee', 'South Hurstville', 'South Maroota', 'South Penrith',
             'South Turramurra', 'South Wentworthville', 'South Windsor', 'Spring Farm', 'St Andrews', 'St Clair',
             'St Helens Park', 'St Ives', 'St Ives Chase', 'St Johns Park', 'St Leonards', 'St Marys', 'St Peters',
             'Stanhope Gardens', 'Stanmore', 'Strathfield', 'Strathfield South', 'Summer Hill', 'Surry Hills',
             'Sutherland', 'Sydenham', 'Sydney Olympic Park', 'Sylvania', 'Sylvania Waters'] \
          + ['Tamarama', 'Taren Point', 'Telopea', 'Tempe', 'Tennyson Point', 'Terrey Hills', 'The Ponds', 'The Rocks',
             'Thornleigh', 'Toongabbie', 'Tregear', 'Turramurra', 'Turrella'] \
          + ['Ultimo'] \
          + ['Varroville', 'Vaucluse', 'Villawood', 'Vineyard', 'Voyager Point'] \
          + ['Wahroonga', 'Waitara', 'Wakeley', 'Wallacia', 'Wareemba', 'Warrawee', 'Warriewood', 'Warwick Farm',
             'Waterfall', 'Waterloo', 'Watsons Bay', 'Wattle Grove', 'Waverley', 'Waverton', 'Weavers', 'Wedderburn',
             'Wentworth Point', 'Wentworthville', 'Werrington', 'Werrington County', 'Werrington Downs', 'West Hoxton',
             'West Killara', 'West Lindfield', 'West Pennant Hills', 'West Pymble', 'West Ryde', 'Westleigh',
             'Westmead', 'Wetherill Park', 'Whalan', 'Wheeler Heights', 'Wiley Park', 'Willmot', 'Willoughby',
             'Willoughby East', 'Windsor', 'Windsor Downs', 'Winston Hills', 'Wisemans Ferry', 'Wolli Creek',
             'Wollstonecraft', 'Woodbine', 'Woodcroft', 'Woodpark', 'Woollahra', 'Woolloomooloo', 'Woolooware',
             'Woolwich', 'Woronora', 'Woronora Heights'] \
          + ['Yagoona', 'Yarramundi', 'Yarrawarrah', 'Yennora', 'Yowie Bay'] \
          + ['Zetland']  ##, 'Prospect'

suburbs = {i.lower() for i in suburbs}

car_type = ['truck', 'ride', 'car', 'cart', 'taxi', 'cab', 'vehicle', 'motorcycle']

car_body_type = ['convertible', 'coupe', 'hatch', 'sedan', 'suv', 'ute', 'van', 'wagon']

car_brand = {'audi', 'bmw', 'ford', 'holden', 'hyundai', 'kia', 'mazda', 'mercedes', 'mitsubishi', 'nissan', 'subaru',
             'toyota', 'volkswagen', 'lexus'}

months = {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
          'october', 'november', 'december'}

'''
car_brand = {'Abarth', 'AC', 'Alfa Romeo', 'Alpina', 'Alpine-Renault', 'Alvis', 'Ariel', 'Armstrong Siddeley',
             'Asia Motors', 'Aston Martin', 'Audi', 'Austin', 'Austin Healey', 'Bentley', 'BMW', 'Bolwell', 'Bond',
             'Bristol', 'Bufori', 'Buick', 'Bullet', 'Cadillac', 'Caterham', 'Chery', 'Chevrolet', 'Chrysler',
             'Citroen', 'Commer', 'Custom', 'Daewoo', 'Daihatsu', 'Daimler', 'Datsun', 'De Tomaso', 'DeSoto', 'DKW',
             'Dodge', 'Durant', 'Eunos', 'Ferrari', 'Fiat', 'Ford', 'Ford Performance Vehicles', 'Foton', 'FSM', 'Fuso',
             'Geely', 'GMC', 'Goliath', 'Great Wall', 'Haval', 'HDT', 'Hillman', 'Hino', 'Holden',
             'Holden Special Vehicles', 'Honda', 'Humber', 'Hummer', 'Hyundai', 'Infiniti', 'International', 'Isuzu',
             'Iveco', 'Jaguar', 'JBA', 'Jeep', 'Jensen', 'JMC', 'Kia', 'KTM', 'Lada', 'Lamborghini', 'Lancia',
             'Land Rover', 'LDV', 'Lexus', 'Leyland', 'Lincoln', 'London Taxi Company', 'Lotus', 'Mahindra', 'Maserati',
             'Mazda', 'McLaren', 'Mercedes-Benz', 'Mercury', 'MG', 'MINI', 'Mitsubishi', 'Morgan', 'Morris', 'Nissan',
             'Oldsmobile', 'Opel', 'Packard', 'Panther', 'Peugeot', 'Plymouth', 'Pontiac', 'Porsche', 'Proton',
             'Purvis', 'RAM', 'Rambler', 'Reliant', 'Renault', 'Riley', 'Robnell', 'Rolls-Royce', 'Rover', 'Saab',
             'Seat', 'SKODA', 'smart', 'SsangYong', 'Studebaker', 'Stutz', 'Subaru', 'Sunbeam', 'Suzuki', 'Tata',
             'Tesla', 'Toyota', 'TRD', 'Triumph', 'TVR', 'U.D.', 'Ultima', 'Vauxhall', 'Volkswagen', 'Volvo',
             'Westfield', 'Willys', 'ZX Auto'}
'''

injury_types = {'head', 'shoulder', 'chest', 'hand', 'neck', 'arm', 'leg', 'face', 'forehead',
                'muscle', 'lung', 'organ', 'skin', 'ear', 'eye', 'limb', 'shoulders', 'hands',
                'arms', 'legs', 'ears', 'eyes', 'limbs', 'injury', 'injured', 'injuries'}

dying_info = {'died', 'death', 'deceased', 'dies', 'decedent', 'dying'}
# died death deceased dies decedent
speeding_keyword = {'speeding', 'exceed', 'chasing'}

limits_keyword = {"limit zone", "school zone", "speed limit"}

common_keywords = {'plaintiff', 'defendant', 'prosecution', 'pardon', 'verdict', 'jury'}

grammar = '''NP:{<.*>+}
                }<PRT>*<ADV>*<VERB>*<ADP>*<PRT>*<ADV>*<VERB>+<ADP>*{
            VP:{<PRT>*<ADV>*<VERB>*<ADP>*<PRT>*<ADV>*<VERB>+<ADP>*}
            '''

date_pattern = r"\d{2}\w\w\s\w*\s\d{4}|\d{2}\s\w*\s\d{4}|\w+\s\d{4}"
money_pattern = r"(\$([0-9]+(\,[0-9]{3}))*(\.[0-9]{1,3})?)"
speed_pattern = r"\d+\s?km/?h|\d+\-\d+\s?km/?h|\d+\s?kp/?h|\d+\-\d+\s?kp/?h|\d+\skilometres per hour|\d+\skms per hour"


def read_file(filename):
    return open(filename).readline()


def line_analysis(line):
    text = line.lower()  # .replace("'s", "")
    result = dict()
    for suburb in suburbs:
        if re.search("\W" + suburb + "\W", text):
            count = text.count(suburb)
            index = [text.find(suburb)]
            for i in range(1, count):
                index.append(text.find(suburb, index[-1] + 1))
            if "suburb" not in result:
                result["suburb"] = dict()
            result["suburb"][suburb] = {"index": index, "length": len(suburb)}
    for ctype in car_type:
        if re.search("\W" + ctype + "\W", text):
            count = text.count(ctype)
            index = [text.find(ctype)]
            for i in range(1, count):
                index.append(text.find(ctype, index[-1] + 1))
            if "car_type" not in result:
                result["car_type"] = dict()
            result["car_type"][ctype] = {"index": index, "length": len(ctype)}
    for sttype in street_type:
        if re.search("\W" + sttype + "\W", text):
            count = text.count(sttype)
            index = [text.find(sttype)]
            for i in range(1, count):
                index.append(text.find(sttype, index[-1] + 1))
            if "street_type" not in result:
                result["street_type"] = dict()
            result["street_type"][sttype] = {"index": index, "length": len(sttype)}
    for brand in car_brand:
        if re.search("\W" + brand + "\W", text):
            count = text.count(brand)
            index = [text.find(brand)]
            for i in range(1, count):
                index.append(text.find(brand, index[-1] + 1))
            if "car_brand" not in result:
                result["car_brand"] = dict()
            result["car_brand"][brand] = {"index": index, "length": len(brand)}
    for cbtype in car_body_type:
        if re.search("\W" + cbtype + "\W", text):
            count = text.count(cbtype)
            index = [text.find(cbtype)]
            for i in range(1, count):
                index.append(text.find(cbtype, index[-1] + 1))
            if "car_body_type" not in result:
                result["car_body_type"] = dict()
            result["car_body_type"][cbtype] = {"index": index, "length": len(cbtype)}
    for injury in injury_types:
        if re.search("\W" + injury + "\W", text):
            count = text.count(injury)
            index = [text.find(injury)]
            for i in range(1, count):
                index.append(text.find(injury, index[-1] + 1))
            if "injury_type" not in result:
                result["injury_type"] = dict()
            result["injury_type"][injury] = {"index": index, "length": len(injury)}
    for key in common_keywords:
        if re.search("\W" + key + "\W", text):
            count = text.count(key)
            index = [text.find(key)]
            for i in range(1, count):
                index.append(text.find(key, index[-1] + 1))
            if "common_keywords" not in result:
                result["common_keywords"] = dict()
            result["common_keywords"][key] = {"index": index, "length": len(key)}
    for zone in limits_keyword:
        if re.search("\W" + zone + "\W", text):
            count = text.count(zone)
            index = [text.find(zone)]
            for i in range(1, count):
                index.append(text.find(zone), index[-1] + 1)
            if "speed_limit" not in result:
                result["speed_limit"] = dict()
            result["speed_limit"][zone] = {"index": index, "length": len(zone)}
    for speeding in speeding_keyword:
        if re.search("\W" + speeding + "\W", text):
            count = text.count(speeding)
            index = [text.find(speeding)]
            for i in range(1, count):
                index.append(text.find(speeding, index[-1] + 1))
            if "speeding_word" not in result:
                result["speeding_word"] = dict()
            result["speeding_word"][speeding] = {"index": index, "length": len(speeding)}
    for info in dying_info:
        if re.search("\W" + info + "\W", text):
            count = text.count(info)
            index = [text.find(info)]
            for i in range(1, count):
                index.append(text.find(info, index[-1] + 1))
            if "dying_info" not in result:
                result["dying_info"] = dict()
            result["dying_info"][info] = {"index": index, "length": len(info)}

    dates = re.findall(date_pattern, text)
    if dates:
        for date in dates:
            for month in months:
                if month in date:
                    count = text.count(date)
                    index = [text.find(date)]
                    for i in range(1, count):
                        index.append(text.find(date, index[-1] + 1))
                    if "dates" not in result:
                        result["dates"] = dict()
                    result["dates"][date] = {"index": index, "length": len(date)}

    moneys = re.findall(money_pattern, text)
    if moneys:
        for money in moneys:
            temp = money[0]
            count = text.count(temp)
            index = [text.find(temp)]
            for i in range(1, count):
                index.append(text.find(temp, index[-1] + 1))
            if "moneys" not in result:
                result["moneys"] = dict()
            result["moneys"][temp] = {"index": index, "length": len(temp)}

    speeds = re.findall(speed_pattern, text)
    if speeds:
        for speed in speeds:
            count = text.count(speed)
            index = [text.find(speed)]
            for i in range(1, count):
                index.append(text.find(speed, index[-1] + 1))
            if "speeds" not in result:
                result["speeds"] = dict()
            result["speeds"][speed] = {"index": index, "length": len(speed)}
    # return result
    return json.dumps(result)


def line_analysis2(line):
    text = line.lower()  # .replace("'s", "")
    result = dict()
    for suburb in suburbs:
        if re.search("\W" + suburb + "\W", text):
            if "suburb" not in result:
                result["suburb"] = []
            result["suburb"].append(suburb)
    for ctype in car_type:
        if re.search("\W" + ctype + "\W", text):
            if "car_type" not in result:
                result["car_type"] = []
            result["car_type"].append(ctype)
    for sttype in street_type:
        if re.search("\W" + sttype + "\W", text):
            if "street_type" not in result:
                result["street_type"] = []
            result["street_type"].append(sttype)
    for brand in car_brand:
        if re.search("\W" + brand + "\W", text):
            if "car_brand" not in result:
                result["car_brand"] = []
            result["car_brand"].append(brand)
    for cbtype in car_body_type:
        if re.search("\W" + cbtype + "\W", text):
            if "car_body_type" not in result:
                result["car_body_type"] = []
            result["car_body_type"].append(cbtype)
    for injury in injury_types:
        if re.search("\W" + injury + "\W", text):
            if "injury_type" not in result:
                result["injury_type"] = []
            result["injury_type"].append(injury)
    for key in common_keywords:
        if re.search("\W" + key + "\W", text):
            if "common_keywords" not in result:
                result["common_keywords"] = []
            result["common_keywords"].append(key)
    for zone in limits_keyword:
        if re.search("\W" + zone + "\W", text):
            if "speed_limit" not in result:
                result["speed_limit"] = []
            result["speed_limit"].append(zone)
    for speeding in speeding_keyword:
        if re.search("\W" + speeding + "\W", text):
            if "speeding_word" not in result:
                result["speeding_word"] = []
            result["speeding_word"].append(speeding)
    for info in dying_info:
        if re.search("\W" + info + "\W", text):
            if "dying_info" not in result:
                result["dying_info"] = []
            result["dying_info"].append(info)

    dates = re.findall(date_pattern, text)
    if dates:
        for date in dates:
            for month in months:
                if month in date:
                    if "dates" not in result:
                        result["dates"] = []
                    result["dates"].append(date)

    moneys = re.findall(money_pattern, text)
    if moneys:
        for money in moneys:
            temp = money[0]
            if "moneys" not in result:
                result["moneys"] = []
            result["moneys"].append(temp)

    speeds = re.findall(speed_pattern, text)
    if speeds:
        for speed in speeds:
            if "speeds" not in result:
                result["speeds"] = []
            result["speeds"].append(speed)
    # return result
    return json.dumps(result)


def file_analysis(filename):
    lines = open(filename, encoding="utf-8").readlines()
    file_result = []
    file_dict = {}
    for i in range(len(lines)):
        line_result = json.loads(line_analysis(lines[i]))
        for key in line_result.keys():
            if key not in file_dict:
                file_dict[key] = []
            file_dict[key].append(i)
        file_result.append(line_result)
    return file_result, file_dict


def json_analysis(jsontext):
    k = json.dumps(jsontext)
    k = json.loads(k)
    k = k['judgment_list']
    re_h = re.compile('</?\w+[^>]*>')
    for i in range(len(k)):
        k[i] = re_h.sub('', k[i])
        k[i] = k[i].replace("\n", ' ')
    return k
