import json

frana = {
    "id": "0250e460-1139-11ea-9245-0242ac120003",
    "active": True,
    "created": "2017-07-18T00:00:00+00:00",
    "modified": "2017-07-18T00:00:00+00:00",
    "point": [
        11.9613385698521,
        44.1030451933667
    ],
    "extent": [
        [
            11.9611459837326,
            44.0993867916258
        ],
        [
            11.9660142094315,
            44.1032249133308
        ]
    ],
    "stato": "importato",
    "nota_rifiuto": None,
    "revision_from": None,
    "revision_validata": None,
    "revision_bozza": None,
    "user": {
        "id": "fbf18866-106d-11ea-89de-0242ac120003",
        "email": "regione.emilia_romagna@isprambiente.it",
        "lastname": "emilia_romagna",
        "firstname": "regione"
    },
    "compilatore_orig": "Servizio Geologico, Sismico e dei Suoli",
    "modified_by": {
        "id": "fbf18866-106d-11ea-89de-0242ac120003",
        "email": "regione.emilia_romagna@isprambiente.it",
        "lastname": "emilia_romagna",
        "firstname": "regione"
    },
    "istituzione": "Regione Emilia-Romagna",
    "istituzione_cf": None,
    "macroregione": 2,
    "regione": 8,
    "provincia": 40,
    "comune": 40032,
    "macroregione_orig": 2,
    "regione_orig": 8,
    "provincia_orig": 40,
    "comune_orig": 40032,
    "autorita_distretto": 2,
    "geom": "SRID=32632;POINT(737014.8349646804 4887582.634893319)",
    "toponimo": None,
    "posizione_punto": None,
    "accuratezza_posizione": None,
    "descrizione": "a1b - Deposito di frana attiva per scivolamento. colamenti lenti di terra e detrito. Creep.",
    "tipo_movimento": 2,
    "data_certa": None,
    "compila_danni": True,
    "personesn": False,
    "feritisn": False,
    "evacuatisn": False,
    "morti": 0,
    "feriti": 0,
    "dispersi": None,
    "evacuati": 0,
    "gruppi_elementi_danni": [
        "8",
        "1",
        "12",
        "2",
        "3",
        "4",
        "9"
    ],
    "elementi_danni": [
        {
            "grado": "5",
            "codice": "56"
        },
        {
            "grado": "3",
            "codice": "23"
        },
        {
            "grado": "4",
            "codice": "1"
        },
        {
            "grado": "3",
            "codice": "58"
        },
        {
            "grado": "1",
            "codice": "10"
        },
        {
            "grado": "5",
            "codice": "55"
        },
        {
            "grado": "4",
            "codice": "11"
        }
    ],
    "danni_acque": {
        "codice": "1",
        "corso_acqua": "Fosso di Predappio"
    },
    "files": [
        {
            "name": "0400011500001.jpg",
            "path": "foto",
            "size": 149444,
            "type": "image/jpeg",
            "mtime": "2004-10-13T13:41:20",
            "url": "https://idrogeo.isprambiente.it/api/media/foto/0400011500001.jpg"
        },
        {
            "name": "0400011500002.pdf",
            "path": "pdf_frane",
            "size": 432268,
            "type": "application/pdf",
            "mtime": "2005-11-21T12:41:38",
            "url": "https://idrogeo.isprambiente.it/api/media/pdf_frane/0400011500002.pdf"
        }
    ],
    "links": None,
    "segnalazione_orig": None,
    "sigla": "PredappioAlta2",
    "data_sopralluogo": None,
    "ex_autorita_bacino": 25,
    "geom_linestring": None,
    "geom_polygon": "SRID=32632;MULTIPOLYGON(((737239.2276947005 4887495.606625182,737245.0680708077 4887495.438623525,737261.0863802505 4887492.817238139,737274.7313909 4887490.849511893,737284.0276820386 4887483.2912276145,737290.3033077874 4887478.536898681,737298.3083853783 4887472.487155652,737306.7446061829 4887466.435965889,737310.0142472818 4887462.686552441,737312.5824648193 4887459.741477492,737313.2171871965 4887448.107553581,737314.0723948296 4887439.91520381,737313.4130286002 4887427.424325879,737308.8445002874 4887408.907286182,737307.6257588144 4887404.603550094,737308.1880673476 4887396.96847135,737310.0734821823 4887389.156295988,737314.6682710003 4887383.214112992,737322.5110483016 4887372.957964037,737330.5828163499 4887367.497028932,737333.4026842369 4887363.508644299,737325.8102196978 4887360.509418972,737320.4346973323 4887345.861743929,737323.0964754093 4887329.858126056,737332.4453223225 4887303.169910099,737345.8068730186 4887269.801198075,737352.4884200478 4887253.782261479,737376.5916190619 4887240.369867715,737400.6939274597 4887225.621168205,737402.6686325612 4887218.908696594,737402.6215574769 4887218.874200122,737397.3928830468 4887208.156039952,737386.3182996928 4887198.247477313,737376.4332179453 4887193.865641982,737364.9045844356 4887188.743526639,737359.9730277606 4887188.186083756,737347.9278588159 4887194.407878622,737342.8792456804 4887199.475039785,737339.8727873309 4887203.391947543,737333.1746614074 4887210.866216055,737323.1887428907 4887218.351376315,737308.2244772445 4887235.0829021735,737293.6207315375 4887255.009545875,737277.5749472246 4887264.6409179075,737245.140847064 4887289.403987674,737233.0218081804 4887300.796058907,737214.4984376174 4887322.495939069,737193.8278974105 4887338.87430498,737183.8487073926 4887348.475718038,737169.9540258896 4887364.480953068,737160.5170475305 4887375.100237836,737151.5404739202 4887386.713510985,737148.4908311842 4887390.652566092,737130.6893326212 4887413.530353885,737110.6519224618 4887436.627479624,737073.2341935836 4887463.298773668,737063.8817864497 4887468.17989279,737052.7466630525 4887472.175422171,737044.7329065952 4887480.604240492,737041.6264300834 4887491.686393901,737044.3144257052 4887501.437538027,737048.3351385037 4887508.083979222,737050.1259519106 4887515.618988622,737048.7970335751 4887523.598622106,737044.3530419338 4887532.023352401,737036.3400092222 4887541.338112559,737018.0803752798 4887552.4386324715,737006.0557078277 4887558.6519406075,737002.0548213031 4887566.19474615,736999.4019483941 4887582.598733727,737000.7521656917 4887595.452651519,737006.9999689562 4887600.767123595,737013.3049797802 4887601.562522107,737024.3826583228 4887602.966845589,737039.0913833703 4887601.180743415,737054.6877572573 4887598.060051868,737070.2815333861 4887592.725498952,737083.6472872131 4887586.060445372,737099.6878724011 4887580.270472997,737108.418179908 4887576.0627858,737112.6111218131 4887574.042681699,737125.977134946 4887567.8111349465,737138.4489867026 4887558.033939606,737154.4820996356 4887543.81265999,737170.0730695974 4887531.591508921,737185.662306979 4887519.589137332,737201.2585980466 4887511.129912397,737215.9641690576 4887504.006255114,737228.8880631711 4887499.093607567,737235.6859168526 4887496.907547043,737239.2276947005 4887495.606625182)))",
    "materiale_1ord": 0,
    "altri_fenomeni": None,
    "stato_attivita_1liv": 100,
    "metodo": [
        "2",
        "4"
    ],
    "data_incerta_min": None,
    "data_incerta_max": None,
    "datazione_attendibile": None,
    "fonti_datazione": [
        "testimonianze",
        "archivi",
        "cartografia"
    ],
    "note_danni": None,
    "costo_beni": None,
    "costo_attivita": None,
    "costo_totale": None,
    "compila_rischio": True,
    "persone_rischiosn": False,
    "persone_rischio": 0,
    "persone_rischio_indirettosn": None,
    "persone_rischio_indiretto": None,
    "ed_privati_rischiosn": True,
    "ed_privati_rischio": 5,
    "ed_pubblici_rischiosn": False,
    "ed_pubblici_rischio": 0,
    "infrastrutture_comunicazione_rischiosn": None,
    "infrastrutture_comunicazione_rischio": None,
    "altro_rischiosn": None,
    "altro_rischio": None,
    "note_rischio": None,
    "volume": None,
    "larghezza": 174,
    "lunghezza": 575,
    "cause": [
        {
            "codice": "12",
            "innescante": False
        },
        {
            "codice": "11",
            "innescante": False
        },
        {
            "codice": "7",
            "innescante": False
        },
        {
            "codice": "1",
            "innescante": False
        },
        {
            "codice": "28",
            "innescante": False
        }
    ],
    "compila_interventi": True,
    "interventi": [
        "10",
        "15",
        "28",
        "5",
        "6"
    ],
    "note_interventi": None,
    "interventi_rendis": None,
    "ad_le_na": "Legge 267/98 PSAI",
    "numero_ord": None,
    "descrizione_ord": None,
    "id_frana": "0400011500",
    "toponimo_ctr": "Predappio",
    "scala_ctr": "10000",
    "numero_ctr": "254080",
    "livello": 3,
    "movimento_1ord": 4,
    "movimento_2ord": 3,
    "velocita_1ord": 0,
    "velocita_2ord": 0,
    "materiale_2ord": 0,
    "acqua_1ord": 0,
    "acqua_2ord": 0,
    "stato_attivita_2liv": 103,
    "data_oss": "20070901",
    "data_oss_certa": None,
    "data_oss_incerta_min": None,
    "data_oss_incerta_max": None,
    "distribuzione": 1,
    "stile": 2,
    "voli": None,
    "eta_radiometrica_anni_bp": None,
    "eta_radiometrica_precisione": None,
    "attivazioni": [
        {
            "id": "806",
            "data": "2003",
            "attendibile": True
        },
        {
            "id": "805",
            "data": "2000",
            "attendibile": True
        },
        {
            "id": "804",
            "data": "1990",
            "attendibile": True
        },
        {
            "id": "803",
            "data": "1934",
            "attendibile": True
        },
        {
            "id": "802",
            "data": "1923",
            "attendibile": True
        },
        {
            "id": "801",
            "data": "1904",
            "attendibile": True
        }
    ],
    "tipi_danno": None,
    "edificisn": True,
    "ed_privatisn": False,
    "ed_privati": 0,
    "ed_pubblicisn": False,
    "ed_pubblici": 0,
    "quota_corona": 291,
    "quota_unghia": 173,
    "dislivello": 118,
    "beta": 11.59708,
    "azimut": 145,
    "area": None,
    "area_calc": 54802.82541322057,
    "dr": None,
    "cod_pos_testata": 3,
    "cod_pos_unghia": 5,
    "cod_esp_ver": 4,
    "uso_suolo": 11,
    "unita_geologiche": [
        {
            "unita": {
                "sigla": "FCO",
                "unita": "88",
                "nome_unita": "FORMAZIONE A COLOMBACCI"
            },
            "assetto": "0",
            "litologia": "16",
            "struttura": "8",
            "spaziatura": "1",
            "descrizione": "FCOb1. Membro conglomeratico frana extraformaz.",
            "litotecnica": "1",
            "degradazione": "3"
        },
        {
            "unita": {
                "sigla": "FCO",
                "unita": "88",
                "nome_unita": "FORMAZIONE A COLOMBACCI"
            },
            "assetto": "9",
            "litologia": "6",
            "struttura": "2",
            "immersione": "135",
            "spaziatura": "3",
            "descrizione": "membro pelitico. Marne argillose e subordinate arenarie. A/P<1.",
            "litotecnica": "1",
            "degradazione": "2",
            "inclinazione": "15"
        }
    ],
    "acque_superficiali": [
        "ruscell_diffuso",
        "ruscell_concentrato"
    ],
    "sorgente": 1,
    "n_sorgente": None,
    "falda": 2,
    "falda_prof": None,
    "segni_precursori": [
        "1"
    ],
    "indagini": [
        "2"
    ],
    "costo_indagini": None,
    "interferometria_sar": None,
    "monitoraggio": None,
    "sistemi_monitoraggio": None,
    "costo_eff_interventi": None,
    "archivio": [
        "2",
        "5"
    ],
    "carg": None,
    "bibliografia": [
        {
            "autori": "SPDS",
            "titolo": "Interventi sul territorio",
            "anno_pubblicazione": "2001"
        },
        {
            "autori": "Zani O.",
            "titolo": "Piano stralcio",
            "anno_pubblicazione": "2001"
        },
        {
            "autori": "Antoniazzi A.",
            "titolo": "Comunità Montana",
            "anno_pubblicazione": "1987"
        },
        {
            "autori": "Raggi B.",
            "titolo": "PSAI",
            "anno_pubblicazione": "1999"
        },
        {
            "autori": "Comune di Predappio",
            "titolo": "PRG",
            "anno_pubblicazione": "2000"
        }
    ]
}

class User:
    def __init__(self, userDict):
        self.userDict = userDict

    def get_id(self) -> str:
        """Get the id of the user."""
        return self.userDict['id']

    def get_email(self) -> str:
        """Get the email of the user."""
        return self.userDict['email'] or None
    
    def get_lastname(self) -> str:
        """Get the lastname of the user."""
        return self.userDict['lastname'] or None
    
    def get_firstname(self) -> str:
        """Get the firstname of the user."""
        return self.userDict['firstname'] or None

# create a class to encode and decode the frana dictionary
class Frana:
    def __init__(self, franaDict):
        self.franaDict = franaDict

    def get_frana_id(self) -> str:
        """Get the id of the frana."""
        return self.franaDict['id_frana']

    def get_system_id(self) -> str:
        """Get the system id of the frana record."""
        return self.franaDict['id']
    
    def get_active(self) -> bool:
        """Get the active status of the frana."""
        return self.franaDict['active']

    def get_created(self) -> str:
        """Get the created date of the frana."""
        return self.franaDict['created']
    
    def get_modified(self) -> str:
        """Get the modified date of the frana."""
        return self.franaDict['modified']
    
    def get_point(self) -> list:
        """Get the point of the frana."""
        return self.franaDict['point'] or None
    
    def get_extent(self) -> list:
        """Get the extent of the frana."""
        return self.franaDict['extent'] or None
    
    def get_stato(self) -> str:
        """Get the stato of the frana."""
        return self.franaDict['stato'] or None
    
    def get_nota_rifiuto(self) -> str:
        """Get the nota_rifiuto of the frana."""
        return self.franaDict['nota_rifiuto'] or None
    
    def get_revision_from(self) -> str:
        """Get the revision_from of the frana."""
        return self.franaDict['revision_from'] or None
    
    def get_revision_validata(self) -> str:
        """Get the revision_validata of the frana."""
        return self.franaDict['revision_validata'] or None
    
    def get_revision_bozza(self) -> str:
        """Get the revision_bozza of the frana."""
        return self.franaDict['revision_bozza'] or None
    
    def get_user(self) -> User:
        """Get the user of the frana."""
        return User(self.franaDict['user']) or None
    
    def get_compilatore_orig(self) -> str:
        """Get the compilatore_orig of the frana."""
        return self.franaDict['compilatore_orig'] or None
    
    def get_modified_by(self) -> User:
        """Get the modified_by of the frana."""
        return User(self.franaDict['modified_by']) or None

    def get_istituzione(self) -> str:
        """Get the istituzione of the frana."""
        return self.franaDict['istituzione'] or None

    def get_istituzione_cf(self) -> str:
        """Get the istituzione_cf of the frana."""
        return self.franaDict['istituzione_cf'] or None
    
    def get_macroregione(self) -> int:
        """Get the macroregione of the frana."""
        return self.franaDict['macroregione'] or None
    
    def get_regione(self) -> int:
        """Get the regione of the frana."""
        return self.franaDict['regione'] or None
    
    def get_provincia(self) -> int:
        """Get the provincia of the frana."""
        return self.franaDict['provincia'] or None
    
    def get_comune(self) -> int:
        """Get the comune of the frana."""
        return self.franaDict['comune'] or None
    
    def get_macroregione_orig(self) -> int:
        """Get the macroregione_orig of the frana."""
        return self.franaDict['macroregione_orig'] or None
    
    def get_regione_orig(self) -> int:
        """Get the regione_orig of the frana."""
        return self.franaDict['regione_orig'] or None
    
    def get_provincia_orig(self) -> int:
        """Get the provincia_orig of the frana."""
        return self.franaDict['provincia_orig'] or None
    
    def get_comune_orig(self) -> int:
        """Get the comune_orig of the frana."""
        return self.franaDict['comune_orig'] or None
    
    def get_autorita_distretto(self) -> int:
        """Get the autorita_distretto of the frana."""
        return self.franaDict['autorita_distretto'] or None
    
    def get_geom_ewkt(self) -> str:
        """Get the geom of the frana."""
        return self.franaDict['geom'] or None
    
    def get_toponimo(self) -> str:
        """Get the toponimo of the frana."""
        return self.franaDict['toponimo'] or None
    



    



