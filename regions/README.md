# Region names and flags

Each country has a folder here with a `regions.json` listing every state, province or region the app knows.
Change a name or pick a flag there, commit, and GitHub rebuilds everything in a minute or two
(watch the **Actions** tab). The app picks up the change the next time it's opened. No app update needed.

Each country folder's page shows every region with its current flag, plus a **To do** list of
regions with no flag and names worth a second look.

## Change a name

```json
"ES-CT": { "name": "Cataluña" }
```

Places you've already marked get the new name too.

## Pick a flag

Three ways, using `"flag"`:

| You write | What it does |
|---|---|
| `"flag": "commons:Flag of Brittany.svg"` | Uses that file from [Wikimedia Commons](https://commons.wikimedia.org) (exact file name, without `File:`). Its license and author are filled in for you. |
| `"flag": "FR-BRE.png"` | Uses an image you uploaded to the same folder (PNG, JPG or SVG; any size, it's scaled down). |
| `"flag": "none"` | Shows no flag for that region. |

Leave `"flag"` out to keep the automatic one (from Wikidata).

For your own uploads, add where it came from, so the credits page stays right:

```json
"FR-BRE": {
  "name": "Bretagne",
  "flag": "FR-BRE.svg",
  "credit": { "author": "…", "license": "Public domain", "source": "https://…" }
}
```

## Editing on github.com

1. Open the country's folder, then `regions.json`, then the pencil icon.
2. Make the change and press **Commit changes**.
3. To add an image: in the country's folder, **Add file → Upload files**.

If something's wrong (a typo in a code, a file that isn't there), the build still publishes everything
else, the Actions run turns red, and the country's page lists the problem at the top.
Watch the commas: every entry but the last ends with one.

## Countries

3202 regions in 197 countries, 1348 with flags.

| Country | Regions | Flags | Missing | Renamed |
|---|---|---|---|---|
| [Andorra](AD/) | 7 | 3 | 4 |  |
| [United Arab Emirates](AE/) | 7 | 7 |  |  |
| [Afghanistan](AF/) | 34 | 0 | 34 |  |
| [Antigua and Barb.](AG/) | 8 | 0 | 8 |  |
| [Albania](AL/) | 12 | 10 | 2 |  |
| [Armenia](AM/) | 11 | 1 | 10 |  |
| [Angola](AO/) | 18 | 0 | 18 |  |
| [Argentina](AR/) | 23 | 23 |  |  |
| [Austria](AT/) | 9 | 9 |  |  |
| [Ashmore and Cartier Is.](AU/) | 9 | 8 | 1 |  |
| [Azerbaijan](AZ/) | 2 | 0 | 2 |  |
| [Bosnia and Herz.](BA/) | 3 | 0 | 3 |  |
| [Barbados](BB/) | 11 | 0 | 11 |  |
| [Bangladesh](BD/) | 8 | 0 | 8 |  |
| [Belgium](BE/) | 3 | 3 |  |  |
| [Burkina Faso](BF/) | 13 | 0 | 13 |  |
| [Bulgaria](BG/) | 28 | 0 | 28 |  |
| [Bahrain](BH/) | 4 | 4 |  |  |
| [Burundi](BI/) | 18 | 0 | 18 |  |
| [Benin](BJ/) | 12 | 0 | 12 |  |
| [Brunei](BN/) | 4 | 0 | 4 |  |
| [Bolivia](BO/) | 9 | 9 |  |  |
| [Brazil](BR/) | 27 | 27 |  |  |
| [Bahamas](BS/) | 32 | 1 | 31 |  |
| [Bhutan](BT/) | 20 | 0 | 20 |  |
| [Botswana](BW/) | 10 | 0 | 10 |  |
| [Belarus](BY/) | 7 | 7 |  |  |
| [Belize](BZ/) | 6 | 0 | 6 |  |
| [Canada](CA/) | 13 | 12 | 1 |  |
| [Dem. Rep. Congo](CD/) | 26 | 1 | 25 |  |
| [Central African Rep.](CF/) | 17 | 0 | 17 |  |
| [Congo](CG/) | 12 | 0 | 12 |  |
| [Switzerland](CH/) | 26 | 26 |  |  |
| [Côte d'Ivoire](CI/) | 14 | 0 | 14 |  |
| [Chile](CL/) | 16 | 0 | 16 |  |
| [Cameroon](CM/) | 10 | 0 | 10 |  |
| [China](CN/) | 31 | 0 | 31 |  |
| [Colombia](CO/) | 33 | 33 |  |  |
| [Costa Rica](CR/) | 7 | 7 |  |  |
| [Cuba](CU/) | 16 | 0 | 16 |  |
| [Cabo Verde](CV/) | 22 | 13 | 9 |  |
| [Cyprus](CY/) | 6 | 0 | 6 |  |
| [Czechia](CZ/) | 14 | 14 |  |  |
| [Germany](DE/) | 16 | 16 |  |  |
| [Djibouti](DJ/) | 6 | 0 | 6 |  |
| [Denmark](DK/) | 5 | 5 |  |  |
| [Dominica](DM/) | 10 | 0 | 10 |  |
| [Dominican Rep.](DO/) | 32 | 1 | 31 |  |
| [Algeria](DZ/) | 48 | 0 | 48 |  |
| [Ecuador](EC/) | 24 | 19 | 5 |  |
| [Estonia](EE/) | 15 | 4 | 11 |  |
| [Egypt](EG/) | 27 | 25 | 2 |  |
| [Eritrea](ER/) | 6 | 0 | 6 |  |
| [Spain](ES/) | 19 | 19 |  |  |
| [Ethiopia](ET/) | 11 | 10 | 1 |  |
| [Finland](FI/) | 18 | 15 | 3 |  |
| [Fiji](FJ/) | 4 | 0 | 4 |  |
| [Micronesia](FM/) | 4 | 4 |  |  |
| [France](FR/) | 18 | 18 |  |  |
| [Gabon](GA/) | 9 | 1 | 8 | 1 |
| [United Kingdom](GB/) | 4 | 3 | 1 |  |
| [Grenada](GD/) | 7 | 0 | 7 |  |
| [Georgia](GE/) | 12 | 3 | 9 |  |
| [Ghana](GH/) | 16 | 4 | 12 |  |
| [Greenland](GL/) | 6 | 2 | 4 |  |
| [Gambia](GM/) | 8 | 1 | 7 |  |
| [Guinea](GN/) | 8 | 0 | 8 |  |
| [Eq. Guinea](GQ/) | 7 | 0 | 7 |  |
| [Greece](GR/) | 14 | 4 | 10 |  |
| [Guatemala](GT/) | 22 | 0 | 22 |  |
| [Guinea-Bissau](GW/) | 9 | 1 | 8 |  |
| [Guyana](GY/) | 10 | 0 | 10 |  |
| [Honduras](HN/) | 18 | 7 | 11 |  |
| [Croatia](HR/) | 21 | 21 |  |  |
| [Haiti](HT/) | 10 | 0 | 10 |  |
| [Hungary](HU/) | 19 | 19 |  |  |
| [Indonesia](ID/) | 34 | 34 |  |  |
| [Ireland](IE/) | 4 | 4 |  |  |
| [Israel](IL/) | 6 | 0 | 6 |  |
| [India](IN/) | 36 | 2 | 34 |  |
| [Iraq](IQ/) | 18 | 0 | 18 |  |
| [Iran](IR/) | 32 | 0 | 32 |  |
| [Iceland](IS/) | 8 | 0 | 8 |  |
| [Italy](IT/) | 20 | 20 |  |  |
| [Jamaica](JM/) | 14 | 0 | 14 |  |
| [Jordan](JO/) | 12 | 0 | 12 |  |
| [Japan](JP/) | 47 | 46 | 1 |  |
| [Kenya](KE/) | 47 | 20 | 27 |  |
| [Kyrgyzstan](KG/) | 7 | 7 |  |  |
| [Cambodia](KH/) | 25 | 0 | 25 |  |
| [Kiribati](KI/) | 3 | 0 | 3 |  |
| [Comoros](KM/) | 3 | 3 |  |  |
| [St. Kitts and Nevis](KN/) | 14 | 0 | 14 |  |
| [North Korea](KP/) | 11 | 0 | 11 |  |
| [South Korea](KR/) | 17 | 15 | 2 |  |
| [Kuwait](KW/) | 6 | 0 | 6 |  |
| [Kazakhstan](KZ/) | 16 | 0 | 16 |  |
| [Laos](LA/) | 18 | 0 | 18 |  |
| [Lebanon](LB/) | 9 | 1 | 8 |  |
| [Saint Lucia](LC/) | 10 | 1 | 9 |  |
| [Liechtenstein](LI/) | 11 | 11 |  |  |
| [Sri Lanka](LK/) | 9 | 9 |  |  |
| [Liberia](LR/) | 15 | 15 |  |  |
| [Lesotho](LS/) | 10 | 0 | 10 |  |
| [Lithuania](LT/) | 10 | 10 |  |  |
| [Luxembourg](LU/) | 12 | 0 | 12 |  |
| [Latvia](LV/) | 43 | 38 | 5 |  |
| [Libya](LY/) | 22 | 0 | 22 |  |
| [Morocco](MA/) | 12 | 1 | 11 |  |
| [Monaco](MC/) | 1 | 0 | 1 |  |
| [Moldova](MD/) | 37 | 34 | 3 |  |
| [Montenegro](ME/) | 23 | 18 | 5 |  |
| [Madagascar](MG/) | 22 | 0 | 22 |  |
| [Marshall Is.](MH/) | 24 | 1 | 23 |  |
| [North Macedonia](MK/) | 8 | 0 | 8 |  |
| [Mali](ML/) | 9 | 0 | 9 |  |
| [Myanmar](MM/) | 14 | 14 |  |  |
| [Mongolia](MN/) | 22 | 22 |  |  |
| [Mauritania](MR/) | 13 | 0 | 13 |  |
| [Malta](MT/) | 68 | 67 | 1 |  |
| [Mauritius](MU/) | 12 | 1 | 11 |  |
| [Maldives](MV/) | 21 | 0 | 21 |  |
| [Malawi](MW/) | 3 | 0 | 3 |  |
| [Mexico](MX/) | 32 | 28 | 4 |  |
| [Malaysia](MY/) | 16 | 16 |  |  |
| [Mozambique](MZ/) | 10 | 3 | 7 |  |
| [Namibia](NA/) | 14 | 0 | 14 |  |
| [Niger](NE/) | 6 | 0 | 6 |  |
| [Nigeria](NG/) | 37 | 14 | 23 |  |
| [Nicaragua](NI/) | 17 | 15 | 2 |  |
| [Netherlands](NL/) | 12 | 12 |  |  |
| [Norway](NO/) | 11 | 8 | 3 |  |
| [Nepal](NP/) | 7 | 0 | 7 |  |
| [Nauru](NR/) | 14 | 0 | 14 |  |
| [Niue](NU/) | 14 | 0 | 14 |  |
| [New Zealand](NZ/) | 17 | 3 | 14 |  |
| [Oman](OM/) | 7 | 0 | 7 |  |
| [Panama](PA/) | 13 | 12 | 1 |  |
| [Peru](PE/) | 26 | 25 | 1 |  |
| [Papua New Guinea](PG/) | 22 | 20 | 2 |  |
| [Philippines](PH/) | 17 | 0 | 17 |  |
| [Pakistan](PK/) | 7 | 5 | 2 |  |
| [Poland](PL/) | 16 | 0 | 16 |  |
| [Palestine](PS/) | 2 | 0 | 2 |  |
| [Portugal](PT/) | 20 | 2 | 18 |  |
| [Palau](PW/) | 16 | 15 | 1 |  |
| [Paraguay](PY/) | 18 | 18 |  |  |
| [Qatar](QA/) | 8 | 0 | 8 |  |
| [Romania](RO/) | 42 | 9 | 33 |  |
| [Serbia](RS/) | 25 | 1 | 24 |  |
| [Russia](RU/) | 83 | 83 |  |  |
| [Rwanda](RW/) | 5 | 0 | 5 |  |
| [Saudi Arabia](SA/) | 13 | 2 | 11 |  |
| [Solomon Is.](SB/) | 10 | 10 |  |  |
| [Seychelles](SC/) | 26 | 0 | 26 |  |
| [Sudan](SD/) | 19 | 9 | 10 |  |
| [Sweden](SE/) | 21 | 20 | 1 |  |
| [Singapore](SG/) | 5 | 0 | 5 |  |
| [Slovenia](SI/) | 2 | 0 | 2 |  |
| [Slovakia](SK/) | 8 | 8 |  |  |
| [Sierra Leone](SL/) | 4 | 0 | 4 |  |
| [San Marino](SM/) | 9 | 9 |  |  |
| [Senegal](SN/) | 14 | 0 | 14 |  |
| [Somalia](SO/) | 18 | 0 | 18 |  |
| [Suriname](SR/) | 10 | 1 | 9 |  |
| [S. Sudan](SS/) | 10 | 10 |  |  |
| [São Tomé and Principe](ST/) | 2 | 1 | 1 |  |
| [El Salvador](SV/) | 14 | 0 | 14 |  |
| [Syria](SY/) | 14 | 0 | 14 |  |
| [eSwatini](SZ/) | 4 | 0 | 4 |  |
| [Chad](TD/) | 23 | 0 | 23 |  |
| [Togo](TG/) | 5 | 0 | 5 |  |
| [Thailand](TH/) | 77 | 70 | 7 |  |
| [Tajikistan](TJ/) | 5 | 0 | 5 |  |
| [Timor-Leste](TL/) | 13 | 1 | 12 |  |
| [Turkmenistan](TM/) | 5 | 0 | 5 |  |
| [Tunisia](TN/) | 24 | 1 | 23 |  |
| [Tonga](TO/) | 5 | 0 | 5 |  |
| [Turkey](TR/) | 81 | 1 | 80 |  |
| [Trinidad and Tobago](TT/) | 14 | 0 | 14 |  |
| [Tuvalu](TV/) | 8 | 0 | 8 |  |
| [Taiwan](TW/) | 22 | 20 | 2 |  |
| [Tanzania](TZ/) | 30 | 0 | 30 |  |
| [Ukraine](UA/) | 27 | 27 |  |  |
| [Uganda](UG/) | 4 | 0 | 4 |  |
| [Uruguay](UY/) | 19 | 17 | 2 |  |
| [Uzbekistan](UZ/) | 14 | 2 | 12 |  |
| [St. Vin. and Gren.](VC/) | 6 | 0 | 6 |  |
| [Venezuela](VE/) | 25 | 24 | 1 |  |
| [Vietnam](VN/) | 64 | 0 | 64 | 1 |
| [Vanuatu](VU/) | 6 | 6 |  |  |
| [Samoa](WS/) | 11 | 0 | 11 |  |
| [Kosovo](XK/) | 7 | 0 | 7 |  |
| [Yemen](YE/) | 22 | 0 | 22 |  |
| [South Africa](ZA/) | 9 | 6 | 3 |  |
| [Zambia](ZM/) | 10 | 0 | 10 |  |
| [Zimbabwe](ZW/) | 10 | 0 | 10 |  |
