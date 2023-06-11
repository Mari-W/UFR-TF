from multiprocessing import Manager


state = Manager().dict()

# TODO: import data/mapping.json..
mapping = {
    "05-968": "\u00c4ltere deutsche Literatur und Sprache",
    "06-772": "Altertumswissenschaften",
    "06-080": "Altertumswissenschaften",
    "06-081": "Altertumswissenschaften",
    "06-629": "Angewandte Politikwissenschaft",
    "07-628": "Applied Physics",
    "06-712": "Arch\u00e4ologische Wissenschaften",
    "06-074": "Arch\u00e4ologische Wissenschaften",
    "06-075": "Arch\u00e4ologische Wissenschaften",
    "06-076": "Arch\u00e4ologische Wissenschaften",
    "06-077": "Arch\u00e4ologische Wissenschaften",
    "03-021": "Betriebswirtschaftslehre",
    "03-621": "Betriebswirtschaftslehre",
    "03-651": "Bildungswissenschaft und Bildungsmanagement",
    "03-751": "Bildungswissenschaft",
    "08-625": "Biochemistry and Biophysics",
    "11-979": "Bioinformatik und Systembiologie",
    "09-026": "Biologie",
    "04-800": "Biomedical Sciences",
    "05-808": "British and North American Cultural Studies",
    "01-863": "Caritaswissenschaft und Ethik",
    "08-032": "Chemie",
    "06-645": "Chinesisch",
    "06-913": "Classical Cultures",
    "05-034": "D\u00e4nisch",
    "05-836": "Deutsch",
    "05-691": "Deutsch",
    "99-752": "Deutsch-Franz\u00f6sische Journalistik",
    "02-635": "Deutsch-Franz\u00f6sisches Recht",
    "05-970": "Deutsche Literatur",
    "05-867": "Deutsche Sprach- und Literaturwissenschaft",
    "93-675": "Economics",
    "93-082": "Economics",
    "93-083": "Economics",
    "93-084": "Economics",
    "11-787": "Embedded Systems Engineering",
    "05-849": "Englisch",
    "05-848": "English and American Studies",
    "05-908": "English Language and Linguistics",
    "05-708": "English Literatures and Literary Theory",
    "10-859": "Environmental Governance",
    "03-052": "Erziehungswissenschaft",
    "06-773": "Ethnologie",
    "05-724": "Europ\u00e4ische Gesellschaften und Kulturen",
    "05-988": "Europ\u00e4ische Literaturen und Kulturen",
    "10-660": "Forstwissenschaften/Forest Sciences",
    "05-839": "FrankoMedia",
    "05-059": "Franz\u00f6sisch",
    "05-671": "Fremdsprache Deutsch",
    "06-850": "Gender Studies",
    "10-050": "Geographie",
    "10-750": "Geographie",
    "10-065": "Geologie",
    "10-665": "Geology",
    "10-765": "Geowissenschaften",
    "05-966": "Germanistik",
    "05-971": "Germanistik",
    "05-670": "Germanistische Linguistik",
    "06-068": "Geschichte",
    "06-730": "Global Urban Health",
    "05-770": "Griechisch",
    "06-613": "Griechisch-r\u00f6mische Arch\u00e4ologie",
    "04-933": "Hebammenwissenschaft",
    "10-956": "Holz- und Bioenergie",
    "10-866": "Hydrologie",
    "05-950": "IberoCultura",
    "05-652": "Indogermanistik",
    "11-079": "Informatik",
    "11-679": "Informatik",
    "11-786": "Intelligente Eingebettete Mikrosysteme",
    "864-1": "Interdiscipry -linEthics",
    "06-930": "Anthropologie",
    "03-932": "Gesundheitsf\u00f6rderung",
    "06-929": "Grundlagen der Politikwissenschaft",
    "99-737": "Interkulturelle Studien",
    "03-878": "International Taxation",
    "10-759": "Internationale Waldwirtschaft",
    "99-937": "Internationale Wirtschaftsbeziehungen",
    "06-083": "Islamwissenschaft",
    "06-886": "Islamwissenschaft",
    "05-084": "Italienisch",
    "06-073": "Judaistik",
    "05-650": "Katalanisch",
    "01-086": "Katholische Theologie",
    "01-688": "Katholisch-Theologische Studien",
    "05-005": "Klassische Philologie",
    "05-079": "Klassische Philologie",
    "05-078": "Klassische Philologie",
    "06-912": "Klassische und Christliche Arch\u00e4ologie",
    "03-732": "Klinische Psychologie",
    "03-832": "Kognitionspsychologie",
    "03-834": "Kognitionswissenschaft",
    "06-774": "Kulturanthropologie",
    "06-674": "Kulturanthropologie",
    "06-092": "Kunstgeschichte",
    "05-895": "Latein",
    "06-604": "Liberal Arts and Sciences",
    "05-954": "Linguistik",
    "05-091": "Linguistik",
    "05-092": "Linguistik",
    "05-093": "Linguistik",
    "05-094": "Linguistik",
    "05-095": "Linguistik",
    "05-096": "Linguistik",
    "05-953": "Linguistik/Linguistics",
    "07-105": "Mathematik",
    "04-707": "Medical Sciences-Cardiovascular Research",
    "05-702": "Medienkulturforschung",
    "05-602": "Medienkulturwissenschaft",
    "04-107": "Medizin",
    "10-110": "Meteorologie und Klimatologie",
    "11-986": "Microsystems Engineering",
    "11-286": "Mikrosystemtechnik",
    "06-612": "Mittelalter- und Renaissance-Studien",
    "05-695": "Mittellateinische Philologie",
    "06-845": "Modern China Studies",
    "06-783": "Moderne islamische Welt",
    "04-807": "Molekulare Medizin",
    "06-114": "Musikwissenschaft",
    "10-893": "Naturschutz und Landschaftspflege",
    "05-667": "Neuere deutsche Literatur, Kultur, Medien",
    "06-768": "Neuere und neueste Geschichte",
    "09-926": "Neuroscience",
    "05-820": "Norwegisch",
    "04-634": "Palliative Care",
    "04-984": "Parodontologie und Implantattherapie",
    "04-985": "Parodontologie und Periimplant\u00e4re Therapie",
    "04-234": "Pflegewissenschaft",
    "08-626": "Pharmazeutische Wissenschaften",
    "08-126": "Pharmazie",
    "06-127": "Philosophie",
    "06-827": "Philosophie/Ethik",
    "07-728": "Physics",
    "07-128": "Physik",
    "06-729": "Politikwissenschaft",
    "06-630": "Politikwissenschaft/Wirtschaftswissenschaft",
    "05-131": "Portugiesisch",
    "03-132": "Psychologie",
    "03-734": "Psychologie",
    "03-934": "Psychology",
    "02-135": "Rechtswissenschaft",
    "08-632": "Regio Chimica",
    "01-136": "Religionswissenschaft",
    "10-857": "Renewable Energy Engineering and Management",
    "05-636": "Romanische Sprachen und Literaturen",
    "05-638": "Romanistik",
    "05-639": "Rum\u00e4nisch",
    "05-139": "Russisch",
    "05-846": "Russlandstudien",
    "05-847": "Russlandstudien",
    "05-821": "Schwedisch",
    "06-145": "Sinologie",
    "05-720": "Skandinavische Literatur- und Kulturgeschichte",
    "05-819": "Skandinavistik",
    "05-146": "Slavische Philologie",
    "05-946": "Slavistik",
    "05-072": "Slavistik",
    "05-071": "Slavistik",
    "05-073": "Slavistik",
    "06-148": "Social Sciences",
    "11-989": "Solar Energy Engineering",
    "06-149": "Soziologie",
    "05-150": "Spanisch",
    "03-831": "Sport",
    "03-828": "Sportwissenschaft",
    "03-829": "Sportwissenschaft",
    "03-830": "Sportwissenschaft",
    "05-771": "Sprachkurs Deutsch",
    "05-967": "Sprachwissenschaft des Deutschen",
    "11-672": "Sustainable System Engineering",
    "08-633": "Sustainable Materials",
    "08-088": "Sustainable Materials",
    "08-087": "Sustainable Materials",
    "08-086": "Sustainable Materials",
    "08-085": "Sustainable Materials",
    "03-978": "Taxation",
    "04-917": "Technische Medizin",
    "10-656": "Umwelthydrologie",
    "10-658": "Umweltnaturwissenschaften",
    "10-760": "Umweltwissenschaften",
    "06-668": "Vergleichende Geschichte der Neuzeit",
    "03-175": "Volkswirtschaftslehre",
    "06-722": "Vorderasiatische Altertumskunde",
    "06-622": "Vorderasiatische Altertumskunde",
    "10-758": "Waldwirtschaft und Umwelt",
    "10-761": "Waldwissenschaften",
    "03-684": "Wirtschaftswissenschaft",
    "04-185": "Zahnmedizin"
}


subjects = {
    "Bildverarbeitung und Computergraphik / Image Processing and Computer Graphics": {
        "type": "Vorlesung"
    },
    "Künstliche Intelligenz / Artificial Intelligence": {
        "type": "Vorlesung"
    },
    "Softwaretechnik / Software Engineering": {"type": "Vorlesung"},
    "Bioinformatik II / Bioinformatics II": {"type": "Vorlesung"},
    "Einführung in die Mobile Robotik / Introduction to Mobile Robotics": {
        "type": "Vorlesung"
    },
    "Modellprädiktive Regelung für erneuerbare Energiesysteme": {"type": "Vorlesung"},
    "Peer-to-Peer Netzwerke / Peer-to-Peer Networks": {"type": "Vorlesung"},
    "SAT Solving": {"type": "Vorlesung"},
    "Verteilte Systeme / Distributed Systems": {"type": "Vorlesung"},
    "Die Provinz Germania superior – die Römer an Ober- und Mittelrhein": {
        "type": "Vorlesung"
    },
    "Archäologie der Merowingerzeit. Kultur und Gesellschaft vom 5. bis 8. Jahrhundert": {
        "type": "Vorlesung"
    },
    "Vergraben - versenkt - verloren. Urgeschichtliche Schatzfunde und ihre Deutung": {
        "type": "Vorlesung"
    },
    "Von Marathon bis Sestos - Die Erinnerung an die Perserkriege": {
        "type": "Vorlesung"
    },
    "Geschichte und Archäologie der Vesuvstädte Teil II": {"type": "Vorlesung"},
    "Einführung in die Byzantinische Archäologie": {"type": "Seminar"},
    "Einführung in die Klassische Archäologie": {"type": "Seminar"},
    "Einführung in die Provinzialrömische Archäologie": {"type": "Seminar"},
    "Kleidung, Fibeln, Identitäten in den römischen Provinzen": {"type": "Seminar"},
    "Megalithen": {"type": "Seminar"},
    "Feuer und Wasser in Frühgeschichte und Mittelalter": {"type": "Seminar"},
    "Einführung Morphologie und Evolution der Pflanzen": {"type": "Vorlesung"},
    "Grundlagen der Mikrobiologie und Immunbiologie": {"type": "Vorlesung"},
    "Grundlagen der Biochemie": {"type": "Vorlesung"},
    "Einführung in die Entwicklungsbiologie": {"type": "Vorlesung"},
    "Einführung in die allgemeine Ökologie": {"type": "Vorlesung"},
    "Einführung in die regionale Vegetationsökologie": {"type": "Vorlesung"},
    "Einführung in die Synthetische Biologie": {"type": "Vorlesung"},
    "Synthetische Gennetzwerke": {"type": "Seminar"},
    "Vom Neuron zur Kognition": {"type": "Seminar"},
    "Einführung in das Modellsystem Arabidopsis thaliana – Ressourcen, Methoden, Entwicklung und Signalmechanismen": {
        "type": "Vorlesung"
    },
    "Ausgesuchte Signalsysteme von Arabidopsis thaliana": {"type": "Seminar"},
    "Altern, Stress und Erkrankung": {"type": "Seminar"},
    "Signalmechanismen bei Stress und Alterung": {"type": "Vorlesung"},
    "Prinzipien der Zell- und Gewebemorphogenese": {"type": "Seminar"},
    "Staatsrecht II": {"type": "Vorlesung"},
    "Informationsrecht": {"type": "Vorlesung"},
    "Telekommunikationsrecht (mit Infrastrukturrecht)": {"type": "Vorlesung"},
    "Kartellrecht": {"type": "Vorlesung"},
    "Schuldrecht I (Allgemeiner Teil)": {"type": "Vorlesung"},
    "Deliktsrecht und Schadensrecht": {"type": "Vorlesung"},
    "Handelsrecht": {"type": "Vorlesung"},
    "Europarecht": {"type": "Vorlesung"},
    "Patentrecht": {"type": "Vorlesung"},
    "Markenrecht": {"type": "Vorlesung"},
    "Europäisches und internationales Recht des geistigen Eigentums": {
        "type": "Vorlesung"
    },
    "Analysis II": {"type": "Vorlesung"},
    "Lineare Algebra II": {"type": "Vorlesung"},
    "Elektrodynamik und Optik": {"type": "Vorlesung"},
    "Einführung in die Elektrotechnik": {"type": "Vorlesung"},
    "Systemtheorie und Regelungstechnik": {"type": "Vorlesung"},
    "Technische Mechanik - Statik": {"type": "Vorlesung"},
    "Werkstoffwissenschaft": {"type": "Vorlesung"},
    "Experimentalphysik II (Elektromagnetismus und Optik)": {"type": "Vorlesung"},
    "Investition und Finanzierung": {"type": "Vorlesung"},
    "Investition und Finanzierung (Tutorate)": {"type": "Lehrveranstaltung"},
    "Mikroökonomik II": {"type": "Vorlesung"},
    "Unternehmensrechnung": {"type": "Vorlesung"},
    "Mathematik II für Studierende der Ingenieurwissenschaften": {
        "type": "Vorlesung"
    },
    "Halbleiterphysik": {"type": "Vorlesung"},
    "Messtechnik": {"type": "Vorlesung"},
    "Angewandte Finite Elemente für die Strukturmechanik": {"type": "Vorlesung"},
    "High-Performance Computing: Fluid Mechanics with Python": {"type": "Vorlesung"},
    "High-Performance Computing: Molecular Dynamics with C++": {"type": "Vorlesung"},
    "Nano-Photonics": {"type": "Vorlesung"},
    "Neurowissenschaften für Ingenieure / Neuroscience for Engineers": {
        "type": "Vorlesung"
    },
    "Signal processing": {"type": "Vorlesung"},
    "Technische Thermodynamik": {"type": "Vorlesung"},
    "Wave Optics": {"type": "Vorlesung"},
    "Holz als Biorohstoff und Energieträger": {"type": "Vorlesung"},
    "Nachwachsende Rohstoffe: Quellen, Eigenschaften und Anwendungen": {
        "type": "Vorlesung"
    },
    "Ökosysteme und Stoffkreisläufe": {"type": "Lehrveranstaltung"},
    "Internationale Politik und Märkte": {"type": "Vorlesung"},
    "Umweltsystemmodellierung": {"type": "Vorlesung"},
    "Einführung in das Management von Non-Profit-Organisationen": {"type": "Vorlesung"},
    "Finanzwissenschaft I (Öffentliche Ausgaben)": {"type": "Vorlesung"},
    "Globalisation, Development and Public Policy": {"type": "Vorlesung"},
    "Grundlagen der Wirtschaftspolitik": {"type": "Vorlesung"},
    "Makroökonomik II": {"type": "Vorlesung"},
    "Ordnungspolitik": {"type": "Vorlesung"},
    "Personal und Organisation": {"type": "Vorlesung"},
    "Charakterisieren des Einflusses von Temperatur und mech. Stress auf die Schwellenspannung von Feldeffekttransistoren": {
        "type": "Projekt"
    },
    "Fit für den Beruf – Grundlagen digitaler Kommunikation und Kollaboration": {
        "type": "Lehrveranstaltung"
    },
    "Grundlagenveranstaltung Nachhaltigkeit – interdisziplinär und reflexiv": {
        "type": "Lehrveranstaltung"
    },
    "Permakultur-Design": {"type": "Lehrveranstaltung"},
    "Nachhaltigkeit aus der Perspektive von Achtsamkeit und Psychologie – eine Einführung": {
        "type": "Lehrveranstaltung"
    },
    "Entrepreneurship for Sustainability: Basics of  impact focused start-ups and enterprises": {
        "type": "Lehrveranstaltung"
    },
    "Spielerische Nachhaltigkeitskommunikation – mit Theater Veränderung anstoßen": {
        "type": "Lehrveranstaltung"
    },
    "Nachhaltigkeit in der Moralfalle? Ansätze der Nachhaltigkeitsethiken": {
        "type": "Lehrveranstaltung"
    },
    "Virtuelle Akademie Nachhaltigkeit": {"type": "Lehrveranstaltung"},
    "Soziale Innovationen und Entrepreneurship im Sport": {"type": "Lehrveranstaltung"},
    "Projektwerkstatt Podcast für die sozial-ökologische Transformation": {
        "type": "Lehrveranstaltung"
    },
    "Globale Lieferketten: Modellierung und Nachhaltigkeitsbewertung": {
        "type": "Lehrveranstaltung"
    },
    "Sustainable Systems Engineering": {"type": "Projekt"},
    "Schaltungstechnik / Circuit Technology": {"type": "Vorlesung"},
    "Nachhaltige Materialien": {"type": "Vorlesung"},
    "Grundlagen resilienter Systeme": {"type": "Vorlesung"},
    "Nachhaltige Energiesysteme": {"type": "Vorlesung"},
    "Für ein erfolgreiches Studium – Selbstorganisation,  Lern- und Arbeitstechniken": {
        "type": "Lehrveranstaltung"
    },
    "Praktikum plus – Kompetenztraining und Berufsfeldorientierung": {
        "type": "Lehrveranstaltung"
    },
    "Effektive Verhandlungsführung": {"type": "Lehrveranstaltung"},
    "REFLECT: Going abroad. Your student exchange capstone module.": {
        "type": "Lehrveranstaltung"
    },
    "Frei Sprechen vor Publikum": {
        "type": "Lehrveranstaltung"
    },
    "Argumentieren in Diskussion und Debatte": {
        "type": "Lehrveranstaltung"
    },
    "Interkulturelle Kompetenzen im globalen Arbeitskontext": {
        "type": "Lehrveranstaltung"
    },
    "Analyse von Life Science Hochdurchsatzdaten mit Galaxy": {
        "type": "Lehrveranstaltung"
    },
    "Advanced Database and Information Systems": {"type": "Lehrveranstaltung"},
    "Numerical Optimal Control in Science and Engineering": {"type": "Vorlesung"},
    "Test und Zuverlässigkeit / Test and Reliability": {"type": "Vorlesung"},
    "Windenergiesysteme / Wind\xa0Energy\xa0Systems": {"type": "Vorlesung"},
    "Embedded Systems Entrepreneurship (2ES)": {"type": "Vorlesung"},
    "Wearable and Implantable Computing (WIC)": {"type": "Vorlesung"},
    "Data Converters": {"type": "Vorlesung"},
    "Micro-actuators": {"type": "Vorlesung"},
    "Optical detector based on digital lock-in amplifiers": {"type": "Projekt"},
    "Kontinuumsmechanik I / Continuum mechanics I": {
        "type": "Vorlesung"
    },
    "Machine Learning Approaches in Structural Mechanics": {"type": "Vorlesung"},
    "Polymer Processing and Microsystems Engineering": {
        "type": "Vorlesung"
    },
    "Biotechnologie für Ingenieurinnen und Ingenieure I: Einführung, Molekular- und Mikrobiologie": {
        "type": "Vorlesung"
    },
    "Biointerfaces II - Interfaces for Bioanalytical Systems": {"type": "Vorlesung"},
    "Microfluidics 1: Effects and Phenomena": {"type": "Vorlesung"},
    "Laser": {"type": "Vorlesung"},
    "Energy and Digitalization": {"type": "Vorlesung"},
    "Funktionalanalysis": {"type": "Vorlesung"},
    "Kommutative Algebra und Einführung in die algebraische Geometrie": {
        "type": "Vorlesung"
    },
    "Kurven und Flächen": {"type": "Vorlesung"},
    "Mathematical Modelling": {"type": "Vorlesung"},
    "Mengenlehre – Unabhängigkeitsbeweise": {"type": "Vorlesung"},
    "Topologie": {"type": "Vorlesung"},
    "Wahrscheinlichkeitstheorie": {"type": "Vorlesung"},
    "Bochner-Räume": {"type": "Vorlesung"},
    "Vorlesung Molekular- und Humangenetik für Molekulare Medizin": {
        "type": "Vorlesung"
    },
    "Konzeption großer Infrastrukturen / Design of Large Infrastructures": {
        "type": "Vorlesung"
    },
    "Model Thinking for Complex Systems": {"type": "Lehrveranstaltung"},
    "Computational Economics": {
        "type": "Vorlesung"
    },
    "Electronic Markets": {"type": "Vorlesung"},
    "Gesundheitsmanagement": {"type": "Vorlesung"},
    "Marketing Management": {"type": "Vorlesung"},
    "Principles of Finance": {"type": "Vorlesung"},
    "Regulation and Competition Policy": {"type": "Vorlesung"},
    "Automatic Mitochondria Segmentation via Transer Learning": {"type": "Projekt"},
    "Masterprojekt SSE / Master Project SSE": {
        "type": "Kolloquium"
    },
    "Solarzellcharakterisierung: Vom Rohmaterial bis zur Zelleffizienz": {
        "type": "Vorlesung"
    },
    "Energie in Gebäuden: Energiebedarf und bauphysikalische Grundlagen / Energy in Buildings: energy demand and building physics": {
        "type": "Vorlesung"
    },
    "Energy System Modeling with Python": {"type": "Lehrveranstaltung"},
    "From the Principles of Re-Design to New Products": {"type": "Vorlesung"},
    "Resilience of Supply Networks": {"type": "Vorlesung"},
    "Numerische Methoden der Materialwissenschaften / Computational Materials Engineering": {
        "type": "Vorlesung"
    },
    "Technische Funktionswerkstoffe": {"type": "Vorlesung"},
    "Material Flow Analysis": {"type": "Lehrveranstaltung"},
    "Bioenergy": {"type": "Lehrveranstaltung"},
    "Climate change: impact, key technologies, and policymaking": {"type": "Vorlesung"},
    "Einführung in die Fachdidaktik der Informatik": {"type": "Vorlesung"},
    "Einführung in die Moraltheologie (M 3)": {"type": "Vorlesung"},
    "Grundlagen der Ethik II: Gewissen-Schuld-Vergebung": {"type": "Vorlesung"},
    "Verantwortung in der Zivilgesellschaft: Focus Technikbewertung, Umweltethik und Nachhaltigkeit": {
        "type": "Seminar"
    },
    "Schulpädagogik": {"type": "Vorlesung"},
    "Zeit- und Selbstmanagement": {"type": "Lehrveranstaltung"},
    "Persönlichkeitsbildung und Rhetorik": {"type": "Lehrveranstaltung"},
    "Grundlagen der Audiotechnik": {"type": "Lehrveranstaltung"},
    "Grundlagen Rhetorik und Präsentation": {"type": "Lehrveranstaltung"},
    "Konflikttraining – Konflikte verstehen und lösen": {"type": "Lehrveranstaltung"},
    "Grundlagen der Filmanalyse – Theorien und Techniken der Filmmontage": {
        "type": "Lehrveranstaltung"
    },
    "Lösungsorientierte Verhandlungs- und Gesprächsführung nach dem Harvard-Konzept": {
        "type": "Lehrveranstaltung"
    },
    "Professionelle Textverarbeitung": {"type": "Lehrveranstaltung"},
    "Informations- und Datenmanagement – Grundlagen im Umgang mit Kundendatenbanken und CRM-Systemen": {
        "type": "Lehrveranstaltung"
    },
    "Grundlagen digitaler Bildbearbeitung": {"type": "Lehrveranstaltung"},
    "Sprechen – Hören – Verstehen – Grundwissen Kommunikation": {
        "type": "Lehrveranstaltung"
    },
    "Textverarbeitung, Tabellenkalkulation, Präsentation – Office-Anwendungen kompakt": {
        "type": "Lehrveranstaltung"
    },
    "Überzeugende Rhetorik – von der Klassik bis zur Gegenwart": {
        "type": "Lehrveranstaltung"
    },
    "Moderation von Konflikten der Stadt-, Raum- und Umweltplanung": {
        "type": "Lehrveranstaltung"
    },
    "Grundlagen Webdesign (Internetpublishing)": {"type": "Lehrveranstaltung"},
    "Kreatives Schreiben – Schreib- und Erzähltechniken": {"type": "Lehrveranstaltung"},
    "Szenisches Erzählen – Charaktere und Dramaturgie": {"type": "Lehrveranstaltung"},
    "Magazinjournalismus in der Praxis – Redaktion und Produktion von Beiträgen für chilli - das Freiburger Stadtmagazin": {
        "type": "Lehrveranstaltung"
    },
    "Verantwortlich handeln – was heißt das? Ethische Fragen in Alltag und Beruf": {
        "type": "Lehrveranstaltung"
    },
    "Writing in English for Professional Purposes": {
        "type": "Lehrveranstaltung"
    },
    "Einführung in die Presse- und Öffentlichkeitsarbeit": {
        "type": "Lehrveranstaltung"
    },
    "Einführung in die Museumspädagogik – Vermittlungs- und Bildungsarbeit im Museum": {
        "type": "Lehrveranstaltung"
    },
    "Einführung in LaTeX für Mathematiker/innen und Naturwissenschaftler/innen": {
        "type": "Lehrveranstaltung"
    },
    "Einführung in das Projektmanagement": {"type": "Lehrveranstaltung"},
    "Basiswissen Betriebswirtschaftslehre": {
        "type": "Lehrveranstaltung"
    },
    "Einführung in den Online-Journalismus": {"type": "Lehrveranstaltung"},
    "Öffentlichkeitsarbeit – Einblicke in die Berufspraxis": {
        "type": "Lehrveranstaltung"
    },
    "Medienarbeit als Teil des Marketings": {"type": "Lehrveranstaltung"},
    "Wissenschaftliches Schreiben – Schreibwerkstatt für Geistes- und Sozialwissenschaftler/innen": {
        "type": "Lehrveranstaltung"
    },
    "Selbstorganisation und Zeitmanagement": {"type": "Lehrveranstaltung"},
    "Portugiesisch I (A0 - A1.1)": {"type": "Lehrveranstaltung"},
    "Portugiesisch II (A1.1 - A1)": {"type": "Lehrveranstaltung"},
    "Einführung in Videoschnitt und Postproduktion": {"type": "Lehrveranstaltung"},
    "Präsentations- und Argumentationstraining": {"type": "Lehrveranstaltung"},
    "Bewerbungskompetenzen – mit Erfolg in den Beruf starten": {
        "type": "Lehrveranstaltung"
    },
    "Grundlagen professioneller Tabellenkalkulation": {"type": "Lehrveranstaltung"},
    "English for Academic Purposes (B2)": {"type": "Lehrveranstaltung"},
    "Einführung in das Betriebssystem Linux": {"type": "Lehrveranstaltung"},
    "Französisch I (A0 - A1.1)": {"type": "Lehrveranstaltung"},
    "Französisch II (A1.1 - A1)": {
        "type": "Lehrveranstaltung"
    },
    "Stimme und Körpersprache in der Präsentation": {"type": "Lehrveranstaltung"},
    "Business English Advanced (B2)": {"type": "Lehrveranstaltung"},
    "Türkisch II (A1.1 - A1.2)": {
        "type": "Lehrveranstaltung"
    },
    "Museums- und Stadtführung in Theorie und Praxis": {"type": "Lehrveranstaltung"},
    "Personale Grundlagen für die Berufsoption Selbständigkeit": {
        "type": "Lehrveranstaltung"
    },
    "Topics in International Development": {"type": "Lehrveranstaltung"},
    "Staats- und Verfassungstheorie": {"type": "Lehrveranstaltung"},
    "Einführung in das Statistikprogramm R (Open Source)": {
        "type": "Lehrveranstaltung"
    },
    "Performance und Präsentation – Stimme, Sprache, Bewegung und Improvisation": {
        "type": "Lehrveranstaltung"
    },
    "Crossmedialer Journalismus in der Praxis – Mitarbeit in der studentischen Redaktion von uniCROSS": {
        "type": "Lehrveranstaltung"
    },
    "Berufsfeld Film- und Fernsehwirtschaft": {"type": "Lehrveranstaltung"},
    "Journalistisches Erzählen – die Reportage": {"type": "Lehrveranstaltung"},
    "Grundlagen des Journalismus": {"type": "Lehrveranstaltung"},
    "Grundlagen der Programmiersprache Python": {"type": "Lehrveranstaltung"},
    "Einführung in die moderne Digitalelektronik": {"type": "Lehrveranstaltung"},
    "Spanisch Konversation II (B2)": {"type": "Lehrveranstaltung"},
    "Diversity-Kompetenz für eine vielfältige Arbeitswelt": {
        "type": "Lehrveranstaltung"
    },
    "Grundlagen der Präsentation und Postererstellung für Naturwissenschaften": {
        "type": "Lehrveranstaltung"
    },
    "Dynamische Websites aufbauen und verwalten mit WordPress": {
        "type": "Lehrveranstaltung"
    },
    "Gründen - aber richtig! Ringvorlesung Entrepreneuship mit Workshopeinheiten": {
        "type": "Lehrveranstaltung"
    },
    "Spanisch Konversation I (B1)": {"type": "Lehrveranstaltung"},
    "Französisch Avancé  (B2 - C1.1)": {
        "type": "Lehrveranstaltung"
    },
    "Transkulturelle Kompetenz in einer globalisierten Welt": {
        "type": "Lehrveranstaltung"
    },
    "Berufsfeld Verlag und Lektorat": {"type": "Lehrveranstaltung"},
    "Spanisch III (A1 - A2.1)": {"type": "Lehrveranstaltung"},
    "Einführung in die Programmierung für Studierende der Naturwissenschaften": {
        "type": "Lehrveranstaltung"
    },
    "Spanisch I (A0 - A1.1)": {"type": "Lehrveranstaltung"},
    "Spanisch II (A1.1 - A1)": {"type": "Lehrveranstaltung"},
    "Spanisch IV (A2.1 - A2)": {"type": "Lehrveranstaltung"},
    "Service Learning – Engagieren, Lernen, Reflektieren": {
        "type": "Lehrveranstaltung"
    },
    "Smartphone- und Web-App-Entwicklung für Programmier-Einsteiger/innen": {
        "type": "Lehrveranstaltung"
    },
    "Praxismodul Entrepreneurship – konkrete Schritte in die unternehmerische Selbstständigkeit": {
        "type": "Lehrveranstaltung"
    },
    "Spanisch V (A2 - B1.1)": {"type": "Lehrveranstaltung"},
    "Intercultural Competence for international Students – How to live and study in Germany": {
        "type": "Lehrveranstaltung"
    },
    "Ökonomie und Verantwortung für Morgen – nachhaltige Wirtschafts- und Lebensstile angesichts der Klimakrise": {
        "type": "Lehrveranstaltung"
    },
    "Redesicherheit und Persönlichkeit – wirksam und überzeugend kommunizieren": {
        "type": "Lehrveranstaltung"
    },
    "Italienisch Konversation (B1)": {"type": "Lehrveranstaltung"},
    "Spanisch VI (B1.1 - B1)": {"type": "Lehrveranstaltung"},
    "Französisch Konversation (B1)": {"type": "Lehrveranstaltung"},
    "Grundlagen des Video-Journalismus": {"type": "Lehrveranstaltung"},
    "Public Relations und interne Unternehmenskommunikation": {
        "type": "Lehrveranstaltung"
    },
    "Italienisch I (A0 - A1.1)": {"type": "Lehrveranstaltung"},
    "Italienisch II (A1.1 - A1.2)": {"type": "Lehrveranstaltung"},
    "Französisch III (A1 - A2.1)": {"type": "Lehrveranstaltung"},
    "Medien in der Praxis – Mitarbeit in einer der studentischen Redaktionen von uniCROSS (Online/Radio/TV/Social Media)": {
        "type": "Lehrveranstaltung"
    },
    "Französisch IV (A2.1 - A2)": {"type": "Lehrveranstaltung"},
    "Französisch V (A2 - B1.1)": {"type": "Lehrveranstaltung"},
    "Grundlagen grafischer Gestaltung kompakt": {"type": "Lehrveranstaltung"},
    "Verantwortung in der Zivilgesellschaft: Focus, Technikbewertung, Umweltethik und Nachhaltigkeit": {
        "type": "Lehrveranstaltung"
    },
    "Programmieren in C/C++": {"type": "Lehrveranstaltung"},
    "Fake News und Co – Grundlagen der angewandten Medienkritik mit Schwerpunkt auf Video- und Filmanalyse": {
        "type": "Lehrveranstaltung"
    },
    "Algorithmen, Google, Facebook und Co – Orientierung in der digitalen Welt": {
        "type": "Lehrveranstaltung"
    },
    "International Relations Management – Einstieg und Erfolg in internationaler, europäischer und grenzüberschreitender Zusammenarbeit": {
        "type": "Lehrveranstaltung"
    },
    "Discover Your Skills – Stärken entdecken und einsetzen": {
        "type": "Lehrveranstaltung"
    },
    "Nachhaltiges Projekt- und Kooperationsmanagement in Non-Profit-Organisationen am Beispiel von Stiftungen": {
        "type": "Lehrveranstaltung"
    },
    "Texten und Storytelling in Social Media": {"type": "Lehrveranstaltung"},
    "Körpersprache - Sprache - Kommunikation – selbstbewusst Auftreten": {
        "type": "Lehrveranstaltung"
    },
    "Probleme lösen und Ideen entwickeln – Einführung in agile, kreative und innovative Methoden": {
        "type": "Lehrveranstaltung"
    },
    "Discover Your Skills.international –  Strengths-based career orientation for international students": {
        "type": "Lehrveranstaltung"
    },
    "Writing in English for Academic Purposes": {"type": "Lehrveranstaltung"},
    "FOSTER Open Science – Student Toolkit": {
        "type": "Lehrveranstaltung"
    },
    "Service Learning.international – Engage. Connect. Reflect.": {
        "type": "Lehrveranstaltung"
    },
    "Digital Studieren: Wie helfen ChatGPT, Zoom & Co. beim mobilen (Zusammen-)Arbeiten und der digitalen Arbeitsorganisation": {
        "type": "Lehrveranstaltung"
    },
    "Critical Media Literacy - Tackling Information Disorder in the Digital Age": {
        "type": "Lehrveranstaltung"
    },
    "Objektorientiertes Programmieren mit Java": {"type": "Lehrveranstaltung"},
    "Grundlagen der künstlichen Intelligenz (KI)": {
        "type": "Lehrveranstaltung"
    },
    "Digitale Gesprächsführung und kollaboratives Arbeiten": {
        "type": "Lehrveranstaltung"
    },
    "Grundlagen Social Media - Kommunikationsstrategien und Kampagnenplanung": {
        "type": "Lehrveranstaltung"
    },
    "Datenanalyse auf Basis von KI-Methoden": {"type": "Lehrveranstaltung"},
    "Karrierechance Unternehmertum – Selbstständigkeit und Unternehmensnachfolge am Beispiel des Handwerks": {
        "type": "Lehrveranstaltung"
    },
    "Partizipative Kulturarbeit – Diversität, Inklusion und Community Building": {
        "type": "Lehrveranstaltung"
    },
    "Ethik als Managementaufgabe und Erfolgsfaktor in Unternehmen": {
        "type": "Lehrveranstaltung"
    },
    "Grundlagen des wissenschaftlichen Schreibens für internationale Studierenden": {
        "type": "Lehrveranstaltung"
    },
    "Geräte und Daten grundlegend schützen": {"type": "Lehrveranstaltung"},
    "Stressmanagement – Strategien erlernen und im Alltag erproben": {
        "type": "Lehrveranstaltung"
    },
    "English for Today’s World: Discussing and debating in professional work settings (B2/C1)": {
        "type": "Lehrveranstaltung"
    },
    "Mathematik II für Studierende der Informatik": {"type": "Vorlesung"},
    "Algorithmen und Datenstrukturen": {"type": "Vorlesung"},
    "Technische Informatik": {"type": "Vorlesung"},
    "Programmieren in C": {"type": "Vorlesung"},
    "Understanding Large Language Models": {"type": "Lehrveranstaltung"},
    "Stochastik für Studierende der Informatik": {"type": "Vorlesung"},
    "Theoretische Informatik": {"type": "Vorlesung"},
    "Graphentheorie": {"type": "Vorlesung"},
    "Assembly and packaing technology": {"type": "Vorlesung"},
    "Oberflächenanalyse / Surface Analysis": {"type": "Vorlesung"},
    "Energy Efficient Power Electronics": {"type": "Vorlesung"},
    "Biomedical Microsystems": {"type": "Vorlesung"},
    "Biomedizinische Messtechnik I / Biomedical Instrumentation I": {
        "type": "Vorlesung"
    },
    "BioMEMS": {"type": "Vorlesung"},
    "Electrochemical energy applications: fuel cells and electrolysis - online": {
        "type": "Vorlesung"
    },
    "Energiegewinnung / Energy harvesting": {"type": "Vorlesung"},
    "Energiespeicherung und Wandlung mittels Brennstoffzellen": {
        "type": "Vorlesung"
    },
    "Entwurf Analoger CMOS Schaltungen / Analog CMOS Circuit Design": {
        "type": "Vorlesung"
    },
    "Advanced Silicon Technology": {"type": "Vorlesung"},
    "Introduction to physiological control systems": {"type": "Vorlesung"},
    "Keramische Werkstoffe der Mikrotechnik": {"type": "Vorlesung"},
    "Lithographie ": {"type": "Vorlesung"},
    "Materials for Electronic Systems": {"type": "Vorlesung"},
    "Mechanischen Eigenschaften und Degradationsmechanismen": {
        "type": "Vorlesung"
    },
    "Mikroakustische Wandler / Micro Acoustical Transducers": {"type": "Vorlesung"},
    "Nanobiotechnologie / Nanobiotechnology": {"type": "Vorlesung"},
    "Nanomaterialien / Nanomaterials": {"type": "Vorlesung"},
    "Nanotechnologie / Nanotechnology": {"type": "Vorlesung"},
    "Optimierung von Fertigungsverfahren / Advanced engineering": {
        "type": "Vorlesung"
    },
    "Optical MEMS": {"type": "Vorlesung"},
    "Optoelectronics": {"type": "Vorlesung"},
    "Quantenmechanik für Ingenieur*innen / Quantum Mechanics for Engineers": {
        "type": "Vorlesung"
    },
    "RF- and Microwave Devices and Circuits": {"type": "Vorlesung"},
    "Sensors and actuators circuit technology": {"type": "Vorlesung"},
    "Sensor-Aktor-Schaltungstechnik": {"type": "Vorlesung"},
    "Signalverarbeitung und Analyse von Gehirnsignalen / Signal processing and analysis in brain signals": {
        "type": "Vorlesung"
    },
    "Spektroskopische Methoden": {"type": "Vorlesung"},
    "Von Mikrosystemen zur Nanowelt / From Microsystems to the Nanoworld": {
        "type": "Vorlesung"
    },
    "Werkstoffdynamik / Dynamics of Materials: Werkstoffcharakterisierung": {
        "type": "Vorlesung"
    },
    "Computational Physics: Materials Science": {"type": "Vorlesung"},
    "Functional Safety, Security and Sustainability: Active Resilience": {
        "type": "Vorlesung"
    },
    "Automated Machine Learning": {"type": "Vorlesung"},
    "Hardware-Praktikum": {"type": "Praktikum"},
    "Reinraumlaborkurs": {"type": "Praktikum"},
    "Messtechnik Praktikum": {"type": "Praktikum"},
    "Praktikum Embedded Systems": {"type": "Praktikum"},
    "Masterpraktikum Deep Learning (Robotics Track)": {"type": "Praktikum"},
    "Praktikum Hardware Security and Trust": {"type": "Praktikum"},
    "Distributed Computing Using Spark": {"type": "Praktikum"},
    "Computer Graphics Project (Rendering Track)": {"type": "Praktikum"},
    "Masterpraktikum Deep Learning (Computer Vision Track)": {"type": "Praktikum"},
    "Praktikum am Lehrstuhl Programmiersprachen": {"type": "Praktikum"},
    "Praktikum am Lehrstuhl Rechnernetze und Telematik": {"type": "Praktikum"},
    "Praktikum am Lehrstuhl für Softwaretechnik": {"type": "Praktikum"},
    "Masterpraktikum Deep Learning (Machine Learning Track)": {"type": "Praktikum"},
    "Praktikum am Lehrstuhl Neurorobotik": {"type": "Praktikum"},
    "Masterpraktikum Deep Learning (Robot Learning Track)": {"type": "Praktikum"},
    "Angewandte Sensorschaltungstechnik": {"type": "Praktikum"},
    "Entwurf Analoger CMOS Schaltungen / Analog CMOS Circuit Design": {
        "type": "Praktikum"
    },
    "Fortgeschrittenes Mikrocontroller-Praktikum": {"type": "Praktikum"},
    "Oberflächenanalyse – Praktikum / Surface Analysis Laboratory": {
        "type": "Praktikum"
    },
    "Optik-Praktikum Grundlagen / Basic Optics Laboratory": {"type": "Praktikum"},
    "Reinraumlaborkurs für Ingenieure / Clean Room Laboratory for Engineers": {
        "type": "Praktikum"
    },
    "Rennautoregelung Praktikum / Race Car Control Laboratory": {"type": "Praktikum"},
    "RF- and Microwave Systems - Design Course": {
        "type": "Praktikum"
    },
    "Technologien der Implantatfertigung / Implant Manufacturing Laboratory": {
        "type": "Praktikum"
    },
    "Biotechnologie für Ingenieurinnen und Ingenieure I: Mikro- und Molekularbiologie": {
        "type": "Praktikum"
    },
    "refining LRAT proofs with CaDiCaL": {"type": "Praktikum"},
    "Introduction to Bioinformatics": {"type": "Seminar"},
    "Introduction to data analysis in bioinformatics": {"type": "Seminar"},
    "Ausgewählte Themen der Computergraphik": {"type": "Seminar"},
    "Automatentheorie": {"type": "Seminar"},
    "Proseminar am Lehrstuhl Neurorobotik": {"type": "Seminar"},
    "Advanced Topics in Animation": {"type": "Seminar"},
    "Advanced Topics in Rendering": {"type": "Seminar"},
    "Current Works in Computer Vision": {"type": "Seminar"},
    "Machine learning in Bioinformatics": {"type": "Seminar"},
    "Blockseminar Deep Learning": {"type": "Seminar"},
    "Seminar Algorithmen für Rechnernetze": {"type": "Seminar"},
    "Principles of Programming Languages": {"type": "Seminar"},
    "Personalization and Recommendation": {"type": "Seminar"},
    "Algorithms and Complexity Reading Group": {"type": "Seminar"},
    "Current Works in Deep Reinforcement Learning": {"type": "Seminar"},
    "Seminar der Mikrosystemtechnik": {"type": "Seminar"},
    "Resilienz und Kollaps ökologisch-ökonomischer Systeme": {
        "type": "Seminar"
    },
    "Studienseminar Sustainable Systems Engineering": {"type": "Seminar"},
    "Nachhaltigkeitskonzepte und -bewertung": {"type": "Seminar"},
    "Technologien Erneuerbarer Energien": {"type": "Seminar"},
    "Ergebnisse wissenschaftlich präsentieren / Scientific writing and presentation": {
        "type": "Seminar"
    },
    "Mikrosystemtechnik in der Medizin": {"type": "Seminar"},
    "Neuroprothetik / Neuroprosthetics": {"type": "Seminar"},
    "Optische Messverfahren: Grundlagen und Anwendungen in der Praxis / Optical measurement techniques": {
        "type": "Seminar"
    },
    "Projektmanagement für Ingenieure / Project management for engineers": {
        "type": "Seminar"
    },
    "Embedded Systems Entrepreneurship (2ES)": {"type": "Seminar"},
    "Learning with Limited Supervision": {"type": "Seminar"},
    "Deep Learning for Tabular Data": {"type": "Seminar"},
    "Gradient-Based Hyperparameter Optimization": {"type": "Seminar"},
    "Solarzellcharakterisierung: Vom Rohmaterial bis zur Zelleffizienz / Characterization of solar cells: From feedstock to final cell efficiency": {
        "type": "Seminar"
    },
}
