import pytz
from django import forms

City: dict[str,str] = {
"Andorra":"AD",
"United Arab Emirates":"AE",
"Afghanistan":"AF",
"Antigua & Barbuda":"AG",
"Anguilla":"AI",
"Albania":"AL",
"Armenia":"AM",
"Angola":"AO",
"Antarctica":"AQ",
"Argentina":"AR",
"Samoa (American)":"AS",
"Austria":"AT",
"Australia":"AU",
"Aruba":"AW",
"Åland Islands":"AX",
"Azerbaijan":"AZ",
"Bosnia & Herzegovina":"BA",
"Barbados":"BB",
"Bangladesh":"BD",
"Belgium":"BE",
"Burkina Faso":"BF",
"Bulgaria":"BG",
"Bahrain":"BH",
"Burundi":"BI",
"Benin":"BJ",
"St Barthelemy":"BL",
"Bermuda":"BM",
"Brunei":"BN",
"Bolivia":"BO",
"Caribbean NL":"BQ",
"Brazil":"BR",
"Bahamas":"BS",
"Bhutan":"BT",
"Bouvet Island":"BV",
"Botswana":"BW",
"Belarus":"BY",
"Belize":"BZ",
"Canada":"CA",
"Cocos (Keeling) Islands":"CC",
"Congo (Dem. Rep.)":"CD",
"Central African Rep.":"CF",
"Congo (Rep.)":"CG",
"Switzerland":"CH",
"Côte d'Ivoire":"CI",
"Cook Islands":"CK",
"Chile":"CL",
"Cameroon":"CM",
"China":"CN",
"Colombia":"CO",
"Costa Rica":"CR",
"Cuba":"CU",
"Cape Verde":"CV",
"Curaçao":"CW",
"Christmas Island":"CX",
"Cyprus":"CY",
"Czech Republic":"CZ",
"Germany":"DE",
"Djibouti":"DJ",
"Denmark":"DK",
"Dominica":"DM",
"Dominican Republic":"DO",
"Algeria":"DZ",
"Ecuador":"EC",
"Estonia":"EE",
"Egypt":"EG",
"Western Sahara":"EH",
"Eritrea":"ER",
"Spain":"ES",
"Ethiopia":"ET",
"Finland":"FI",
"Fiji":"FJ",
"Falkland Islands":"FK",
"Micronesia":"FM",
"Faroe Islands":"FO",
"France":"FR",
"Gabon":"GA",
"Britain (UK)":"GB",
"Grenada":"GD",
"Georgia":"GE",
"French Guiana":"GF",
"Guernsey":"GG",
"Ghana":"GH",
"Gibraltar":"GI",
"Greenland":"GL",
"Gambia":"GM",
"Guinea":"GN",
"Guadeloupe":"GP",
"Equatorial Guinea":"GQ",
"Greece":"GR",
"South Georgia & the South Sandwich Islands":"GS",
"Guatemala":"GT",
"Guam":"GU",
"Guinea-Bissau":"GW",
"Guyana":"GY",
"Hong Kong":"HK",
"Heard Island & McDonald Islands":"HM",
"Honduras":"HN",
"Croatia":"HR",
"Haiti":"HT",
"Hungary":"HU",
"Indonesia":"ID",
"Ireland":"IE",
"Israel":"IL",
"Isle of Man":"IM",
"India":"IN",
"British Indian Ocean Territory":"IO",
"Iraq":"IQ",
"Iran":"IR",
"Iceland":"IS",
"Italy":"IT",
"Jersey":"JE",
"Jamaica":"JM",
"Jordan":"JO",
"Japan":"JP",
"Kenya":"KE",
"Kyrgyzstan":"KG",
"Cambodia":"KH",
"Kiribati":"KI",
"Comoros":"KM",
"St Kitts & Nevis":"KN",
"Korea (North)":"KP",
"Korea (South)":"KR",
"Kuwait":"KW",
"Cayman Islands":"KY",
"Kazakhstan":"KZ",
"Laos":"LA",
"Lebanon":"LB",
"St Lucia":"LC",
"Liechtenstein":"LI",
"Sri Lanka":"LK",
"Liberia":"LR",
"Lesotho":"LS",
"Lithuania":"LT",
"Luxembourg":"LU",
"Latvia":"LV",
"Libya":"LY",
"Morocco":"MA",
"Monaco":"MC",
"Moldova":"MD",
"Montenegro":"ME",
"St Martin (French)":"MF",
"Madagascar":"MG",
"Marshall Islands":"MH",
"North Macedonia":"MK",
"Mali":"ML",
"Myanmar (Burma)":"MM",
"Mongolia":"MN",
"Macau":"MO",
"Northern Mariana Islands":"MP",
"Martinique":"MQ",
"Mauritania":"MR",
"Montserrat":"MS",
"Malta":"MT",
"Mauritius":"MU",
"Maldives":"MV",
"Malawi":"MW",
"Mexico":"MX",
"Malaysia":"MY",
"Mozambique":"MZ",
"Namibia":"NA",
"New Caledonia":"NC",
"Niger":"NE",
"Norfolk Island":"NF",
"Nigeria":"NG",
"Nicaragua":"NI",
"Netherlands":"NL",
"Norway":"NO",
"Nepal":"NP",
"Nauru":"NR",
"Niue":"NU",
"New Zealand":"NZ",
"Oman":"OM",
"Panama":"PA",
"Peru":"PE",
"French Polynesia":"PF",
"Papua New Guinea":"PG",
"Philippines":"PH",
"Pakistan":"PK",
"Poland":"PL",
"St Pierre & Miquelon":"PM",
"Pitcairn":"PN",
"Puerto Rico":"PR",
"Palestine":"PS",
"Portugal":"PT",
"Palau":"PW",
"Paraguay":"PY",
"Qatar":"QA",
"Réunion":"RE",
"Romania":"RO",
"Serbia":"RS",
"Russia":"RU",
"Rwanda":"RW",
"Saudi Arabia":"SA",
"Solomon Islands":"SB",
"Seychelles":"SC",
"Sudan":"SD",
"Sweden":"SE",
"Singapore":"SG",
"St Helena":"SH",
"Slovenia":"SI",
"Svalbard & Jan Mayen":"SJ",
"Slovakia":"SK",
"Sierra Leone":"SL",
"San Marino":"SM",
"Senegal":"SN",
"Somalia":"SO",
"Suriname":"SR",
"South Sudan":"SS",
"Sao Tome & Principe":"ST",
"El Salvador":"SV",
"St Maarten (Dutch)":"SX",
"Syria":"SY",
"Eswatini (Swaziland)":"SZ",
"Turks & Caicos Is":"TC",
"Chad":"TD",
"French Southern Territories":"TF",
"Togo":"TG",
"Thailand":"TH",
"Tajikistan":"TJ",
"Tokelau":"TK",
"East Timor":"TL",
"Turkmenistan":"TM",
"Tunisia":"TN",
"Tonga":"TO",
"Turkey":"TR",
"Trinidad & Tobago":"TT",
"Tuvalu":"TV",
"Taiwan":"TW",
"Tanzania":"TZ",
"Ukraine":"UA",
"Uganda":"UG",
"US minor outlying islands":"UM",
"United States":"US",
"Uruguay":"UY",
"Uzbekistan":"UZ",
"Vatican City":"VA",
"St Vincent":"VC",
"Venezuela":"VE",
"Virgin Islands (UK)":"VG",
"Virgin Islands (US)":"VI",
"Vietnam":"VN",
"Vanuatu":"VU",
"Wallis & Futuna":"WF",
"Samoa (western)":"WS",
"Yemen":"YE",
"Mayotte":"YT",
"South Africa":"ZA",
"Zambia":"ZM",
"Zimbabwe":"ZW",
}

Zone = pytz.all_timezones

Region =[
        ('', 'Тут можно найти нужный город'),
    ('Europe', (
            ('Europe/Amsterdam', 'Amsterdam'),
            ('Europe/Andorra', 'Andorra'),
            ('Europe/Astrakhan', 'Astrakhan'),
            ('Europe/Athens', 'Athens'),
            ('Europe/Belfast', 'Belfast'),
            ('Europe/Belgrade', 'Belgrade'),
            ('Europe/Berlin', 'Berlin'),
            ('Europe/Bratislava', 'Bratislava'),
            ('Europe/Bucharest', 'Bucharest'),
            ('Europe/Budapest','Budapest'),
            ('Europe/Busingen','Busingen'),
            ('Europe/Chisinau','Chisinau'),
            ('Europe/Copenhagen','Copenhagen'),
            ('Europe/Dublin','Dublin'),
            ('Europe/Gibraltar','Gibraltar'),
            ('Europe/Guernsey','Guernsey'),
            ('Europe/Helsinki','Helsinki'),
            ('Europe/Isle_of_Man','Isle_of_Man'),
            ('Europe/Istanbul','Istanbul'),
            ('Europe/Jersey','Jersey'),
            ('Europe/Kaliningrad','Kaliningrad'),
            ('Europe/Kiev','Kiev'),
            ('Europe/Kiev','Kirov'),
            ('Europe/Lisbon','Lisbon'),
            ('Europe/Ljubljana','Ljubljana'),
            ('Europe/London','London'),
            ('Europe/Luxembourg','Luxembourg'),
            ('Europe/Madrid','Madrid'),
            ('Europe/Malta','Malta'),
            ('Europe/Mariehamn','Mariehamn'),
            ('Europe/Minsk','Minsk'),
            ('Europe/Monaco','Monaco'),
            ('Europe/Moscow','Moscow'),
            ('Europe/Nicosia','Nicosia'),
            ('Europe/Oslo','Oslo'),
            ('Europe/Paris','Paris'),
            ('Europe/Podgorica','Podgorica'),
            ('Europe/Prague','Prague'),
            ('Europe/Riga','Riga'),
            ('Europe/Rome','Rome'),
            ('Europe/Samara','Samara'),
            ('Europe/San_Marino','San_Marino'),
            ('Europe/Sarajevo','Sarajevo'),
            ('Europe/Saratov','Saratov'),
            ('Europe/Simferopol','Simferopol'),
            ('Europe/Skopje','Skopje'),
            ('Europe/Sofia','Sofia'),
            ('Europe/Stockholm','Stockholm'),
            ('Europe/Tallinn','Tallinn'),
            ('Europe/Tirane','Tirane'),
            ('Europe/Tiraspol','Tiraspol'),
            ('Europe/Ulyanovsk','Ulyanovsk'),
            ('Europe/Uzhgorod','Uzhgorod'),
            ('Europe/Vaduz','Vaduz'),
            ('Europe/Vatican','Vatican'),
            ('Europe/Vienna','Vienna'),
            ('Europe/Vilnius','Vilnius'),
            ('Europe/Volgograd','Volgograd'),
            ('Europe/Warsaw','Warsaw'),
            ('Europe/Zagreb','Zagreb'),
            ('Europe/Zaporozhye','Zaporozhye'),
            ('Europe/Zurich','Zurich'),
        )
    ),
    ]

Region_us =[
            ('', 'Тут можно найти нужный город'),
    ('America', (
            ('America/Adak','Adak'),
            ('America/Anchorage','Anchorage'),
            ('America/Anguilla','Anguilla'),
            ('America/Antigua','Antigua'),
            ('America/Araguaina','Araguaina'),
            ('America/Argentina/Buenos_Aires','Buenos_Aires'),
            ('America/Argentina/Catamarca','Catamarca'),
            ('America/Argentina/ComodRivadavia','ComodRivadavia'),
            ('America/Argentina/Cordoba','Cordoba'),
            ('America/Argentina/Jujuy','Jujuy'),
            ('America/Argentina/La_Rioja','La_Rioja'),
            ('America/Argentina/Mendoza','Mendoza'),
            ('America/Argentina/Rio_Gallegos','Rio_Gallegos'),
            ('America/Argentina/Salta','Salta'),
            ('America/Argentina/San_Juan','San_Juan'),
            ('America/Argentina/San_Luis','San_Luis'),
            ('America/Argentina/Tucuman','Tucuman'),
            ('America/Argentina/Ushuaia','Ushuaia'),
            ('America/Aruba','Aruba'),
            ('America/Asuncion','Asuncion'),
            ('America/Atikokan','Atikokan'),
            ('America/Atka','Atka'),
            ('America/Bahia','Bahia'),
            ('America/Bahia_Banderas','Bahia_Banderas'),
            ('America/Barbados','Barbados'),
            ('America/Belem','Belem'),
            ('America/Belize','Belize'),
            ('America/Blanc-Sablon','Blanc-Sablon'),
            ('America/Boa_Vista','Boa_Vista'),
            ('America/Bogota','Bogota'),
            ('America/Boise','Boise'),
            ('America/Buenos_Aires','Buenos_Aires'),
            ('America/Cambridge_Bay','Cambridge_Bay'),
            ('America/Campo_Grande','Campo_Grande'),
            ('America/Cancun','Cancun'),
            ('America/Caracas','Caracas'),
            ('America/Catamarca','Catamarca'),
            ('America/Cayenne','Cayenne'),
            ('America/Cayman','Cayman'),
            ('America/Chicago','Chicago'),
            ('America/Chihuahua','Chihuahua'),
            ('America/Ciudad_Juarez','Ciudad_Juarez'),
            ('America/Coral_Harbour','Coral_Harbour'),
            ('America/Cordoba','Cordoba'),
            ('America/Costa_Rica','Costa_Rica'),
            ('America/Creston','Creston'),
            ('America/Cuiaba','Cuiaba'),
            ('America/Curacao','Curacao'),
            ('America/Danmarkshavn','Danmarkshavn'),
            ('America/Dawson','Dawson'),
            ('America/Dawson_Creek','Dawson_Creek'),
            ('America/Denver','Denver'),
            ('America/Detroit','Detroit'),
            ('America/Dominica','Dominica'),
            ('America/Edmonton','Edmonton'),
            ('America/Eirunepe','Eirunepe'),
            ('America/El_Salvador','El_Salvador'),
            ('America/Ensenada','Ensenada'),
            ('America/Fort_Nelson','Fort_Nelson'),
            ('America/Fort_Wayne','Fort_Wayne'),
            ('America/Fortaleza','Fortaleza'),
            ('America/Glace_Bay','Glace_Bay'),
            ('America/Godthab','Godthab'),
            ('America/Goose_Bay','Goose_Bay'),
            ('America/Grand_Turk','Grand_Turk'),
            ('America/Grenada','Grenada'),
            ('America/Guadeloupe','Guadeloupe'),
            ('America/Guatemala','Guatemala'),
            ('America/Guayaquil','Guayaquil'),
            ('America/Guyana','Guyana'),
            ('America/Halifax','Halifax'),
            ('America/Kentucky/Louisville','Kentucky/Louisville'),
            ('America/Lima','Lima'),
            ('America/Los_Angeles','Los_Angeles'),
            ('America/Menominee','Menominee'),
            ('America/Merida','Merida'),
            ('America/Mexico_City','Mexico_City'),
            ('America/Miquelon','Miquelon'),
            ('America/New_York','New_York'),
            ('America/Nipigon', 'Nipigon'),
            ('America/Puerto_Rico','Puerto_Rico'),
            ('America/Punta_Arenas','Punta_Arenas'),
            ('America/Santiago','Santiago'),
            ('America/Santo_Domingo','Santo_Domingo'),
            ('America/Sao_Paulo','Sao_Paulo'),
            ('America/Winnipeg','Winnipeg'),
            ('America/Yakutat','Yakutat'),
        )
    ),
    ]


class ZoneForm(forms.Form):
    region = forms.ChoiceField(choices = Region)


class ZoneFormUSA(forms.Form):
    region_US = forms.ChoiceField(choices=Region_us)