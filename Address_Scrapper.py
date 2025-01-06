import csv

# Raw tab-separated data
data = """
Safeway	Q01036	2227 S Shore Center	Alameda, CA
Food 4 Less	Q00330	1616 W Katella Ave	Anaheim, CA
Albertsons	Q00491	810 S State College Blvd	Anaheim, CA
Vons	Q00695	5600 Santa Ana Canyon Rd	Anaheim, CA
Vons	Q00715	745 W Naomi Ave	Arcadia, CA
Safeway	Q00918	2550 Bell Rd	Auburn, CA
Food 4 Less	Q00711	6901 Eastern Ave	Bell Gardens, CA
Safeway	Q01020	1444 Shattuck Pl	Berkeley, CA
Vons	Q00314	301 N Pass Ave	Burbank, CA
Albertsons	Q00523	26521 Agoura Rd	Calabasas, CA
Safeway	Q00974	3380 Coach Ln	Cameron Park, CA
Vons	Q00875	2560 El Camino Real	Carlsbad, CA
Vons	Q01024	6951 El Camino Real	Carlsbad, CA
Safeway	Q00989	4040 Manzanita Ave	Carmichael, CA
Albertsons	Q00722	200 E Sepulveda Blvd	Carson, CA
Safeway	Q01102	4015 E Castro Valley Blvd	Castro Valley, CA
Vons	Q00331	1745 Eastlake Pkwy	Chula Vista, CA
Vons	Q01032	2250 Otay Lakes Rd	Chula Vista, CA
Safeway	Q00941	7301 Greenback Ln	Citrus Heights, CA
Food 4 Less	Q00409	1900 W Rosecrans Ave	Compton, CA
Safeway	Q00970	2600 Willow Pass Rd	Concord, CA
Albertsons	Q00388	260 W Foothill Pkwy	Corona, CA
Vons	Q00508	535 N McKinley St	Corona, CA
Vons	Q00511	11800 De Palma Rd	Corona, CA
Safeway	Q01151	3496 Camino Tassajara	Danville, CA
Food 4 Less	Q00311	13525 Lakewood Blvd	Downey, CA
Ralphs	Q00739	8626 Firestone Blvd	Downey, CA
Safeway	Q00928	7499 Dublin Blvd	Dublin, CA
Safeway	Q00930	4440 Tassajara Rd	Dublin, CA
Albertsons	Q00655	7070 Archibald Ave	Eastvale, CA
Vons	Q01167	6170 Hamner Ave	Eastvale, CA
Albertsons	Q00474	1608 Broadway	El Cajon, CA
Vons	Q00886	1201 Avocado Ave	El Cajon, CA
Albertsons	Q01247	2899 Jamacha Rd	El Cajon, CA
Safeway	Q01018	11450 San Pablo Ave	El Cerrito, CA
Safeway	Q00938	2207 Francisco Dr	El Dorado Hills, CA
Safeway	Q00977	3383 Bass Lake Rd	El Dorado Hills, CA
Safeway	Q00931	5021 Laguna Blvd	Elk Grove, CA
Pak N Save	Q01060	3889 San Pablo Ave	Emeryville, CA
Albertsons	Q00890	1570 W Valley Pkwy	Escondido, CA
Vons	Q00892	1000 W El Norte Pkwy	Escondido, CA
Vons	Q01030	351 W Felicita Ave	Escondido, CA
Food 4 Less	Q01250	644 N Broadway	Escondido, CA
Safeway	Q00943	5450 Dewey Dr	Fair Oaks, CA
Albertsons	Q00476	1133 S Mission Rd	Fallbrook, CA
Safeway	Q00981	1850 Prairie City Rd	Folsom, CA
Vons	Q00563	7390 Cherry Ave	Fontana, CA
Albertsons	Q00328	16061 Brookhurst St	Fountain Valley, CA
Safeway	Q00973	39100 Argonaut Way	Fremont, CA
Safeway	Q01026	3902 Washington Blvd	Fremont, CA
Albertsons	Q00332	1930 N Placentia Ave	Fullerton, CA
Vons	Q00717	11861 Valley View St	Garden Grove, CA
Vons	Q00658	1260 W Redondo Beach Blvd	Gardena, CA
Albertsons	Q00732	1735 W Artesia Blvd	Gardena, CA
Food 4 Less	Q01249	1299 W Artesia Blvd	Gardena, CA
Vons	Q00417	561 N Glendale Ave	Glendale, CA
Vons	Q00699	311 W Los Feliz Rd	Glendale, CA
Albertsons	Q00427	133 W Route 66	Glendora, CA
Vons	Q00707	2122 S Hacienda Blvd	Hacienda Heights, CA
Food 4 Less	Q00315	14500 Ocean Gate Ave	Hawthorne, CA
FoodMaxx	Q01041	27300 Hesperian Blvd	Hayward, CA
Safeway	Q01051	22280 Foothill Blvd	Hayward, CA
Safeway	Q00939	4080 San Pablo Ave	Hercules, CA
Vons	Q00721	715 Pier Ave	Hermosa Beach, CA
Vons	Q00322	5922 Edinger Ave	Huntington Beach, CA
Albertsons	Q00325	7201 Yorktown Ave	Huntington Beach, CA
Albertsons	Q00483	19640 Beach Blvd	Huntington Beach, CA
Food 4 Less	Q00418	6920 Santa Fe Ave	Huntington Park, CA
Food 4 Less	Q00380	3200 W Century Blvd	Inglewood, CA
Vons	Q00422	500 E Manchester Blvd	Inglewood, CA
Albertsons	Q00416	14201 Jeffrey Rd	Irvine, CA
Albertsons	Q00590	4541 Campus Dr	Irvine, CA
Safeway	Q00922	12110 Industry Blvd	Jackson, CA
Albertsons	Q00583	1800 W Whittier Blvd	La Habra, CA
Albertsons	Q00878	8920 Fletcher Pkwy	La Mesa, CA
Food 4 Less	Q00338	1821 N Hacienda Blvd	La Puente, CA
Albertsons	Q01007	30241 Golden Lantern	Laguna Niguel, CA
Albertsons	Q00518	30901 Riverside Dr	Lake Elsinore, CA
Vons	Q00317	4226 Woodruff Ave	Lakewood, CA
Vons	Q00740	5500 Woodruff Ave	Lakewood, CA
Safeway	Q00987	1554 1st St	Livermore, CA
Safeway	Q01049	4495 1st St	Livermore, CA
Vons	Q00654	1800-2000 Ximeno Ave	Long Beach, CA
Food 4 Less	Q00720	3210 E Anaheim St	Long Beach, CA
Albertsons	Q01019	101 E Willow St	Long Beach, CA
Food 4 Less	Q00319	9635 Laurel Canyon Blvd	Los Angeles, CA
Food 4 Less	Q00324	5100 N Figueroa St	Los Angeles, CA
Vons	Q00336	3461 W 3rd St	Los Angeles, CA
Food 4 Less	Q00370	16530 Sherman Way	Los Angeles, CA
Food 4 Less	Q00386	11507 S Western Ave	Los Angeles, CA
Food 4 Less	Q00391	11840 Wilmington Ave	Los Angeles, CA
Food 4 Less	Q00410	336 W Anaheim St	Los Angeles, CA
Food 4 Less	Q00411	18318 Vanowen St	Los Angeles, CA
Food 4 Less	Q00413	1820 W Slauson Ave	Los Angeles, CA
Food 4 Less	Q00419	16208 Parthenia St	Los Angeles, CA
Food 4 Less	Q00420	2750 E 1st St	Los Angeles, CA
Vons	Q00425	4520 W Sunset Blvd	Los Angeles, CA
Pavilions	Q00469	14845 Ventura Blvd	Los Angeles, CA
Vons	Q00702	16830 San Fernando Mission Blvd	Los Angeles, CA
Vons	Q00719	7311 N Figueroa St	Los Angeles, CA
Safeway	Q00983	15549 Union Ave	Los Gatos, CA
Safeway	Q00980	1187 S Main St	Manteca, CA
Pavilions	Q00512	4365 Glencoe Ave	Marina del Rey, CA
Safeway	Q00982	555 E Calaveras Blvd	Milpitas, CA
Albertsons	Q00575	23072 Alicia Pkwy	Mission Viejo, CA
Vons	Q00335	130 W Foothill Blvd	Monrovia, CA
Albertsons	Q00704	2469 Via Campo	Montebello, CA
Safeway	Q00932	235 Tennant Station	Morgan Hill, CA
Safeway	Q00985	840 E Dunne Ave	Morgan Hill, CA
Albertsons	Q00495	41000 California Oaks Rd	Murrieta, CA
Pavilions	Q00995	21181 Newport Coast Dr	Newport Beach, CA
FoodMaxx	Q00984	3000 E 9th St	Oakland, CA
Safeway	Q01164	4100 Redwood Rd	Oakland, CA
Albertsons	Q00668	3450 Marron Rd	Oceanside, CA
Albertsons	Q00751	4150 Oceanside Blvd	Oceanside, CA
Vons	Q01005	845 College Blvd	Oceanside, CA
Food 4 Less	Q01176	2246 S Euclid Ave	Ontario, CA
Vons	Q00591	2684 N Tustin Ave	Orange, CA
Vons	Q00494	2101 N Rose Ave	Oxnard, CA
Vons	Q00372	2355 E Colorado Blvd	Pasadena, CA
Safeway	Q00969	3955 Missouri Flat Rd	Placerville, CA
Safeway	Q00967	600 Patterson Blvd	Pleasant Hill, CA
Safeway	Q01031	1978 Contra Costa Blvd	Pleasant Hill, CA
Safeway	Q01148	707 Contra Costa Blvd	Pleasant Hill, CA
Safeway	Q00944	1701 Santa Rita Rd	Pleasanton, CA
Safeway	Q00935	10635 Folsom Blvd	Rancho Cordova, CA
Albertsons	Q00510	450 E Cypress Ave	Redlands, CA
Vons	Q00741	4001 Inglewood Ave	Redondo Beach, CA
Albertsons	Q00500	2975 Van Buren Blvd	Riverside, CA
Vons	Q01097	3520 Riverside Plaza	Riverside, CA
Safeway	Q00631	2220 Sunset Blvd	Rocklin, CA
Pavilions	Q00714	7 Peninsula Center	Rolling Hills Estates, CA
Safeway	Q00923	8640 Sierra College Blvd	Roseville, CA
Safeway	Q00927	1080 Pleasant Grove Blvd	Roseville, CA
Safeway	Q00929	989 Sunrise Ave	Roseville, CA
Safeway	Q00988	9045 Woodcreek Oaks Blvd	Roseville, CA
Safeway	Q00924	1814 19th St	Sacramento, CA
Safeway	Q00926	1025 Alhambra Blvd	Sacramento, CA
Safeway	Q00933	3320 Arden Way	Sacramento, CA
Safeway	Q00968	8377 Elk Grove Florin Rd	Sacramento, CA
Vons	Q00489	620 Dennery Rd	San Diego, CA
Vons	Q00492	11986 Bernardo Plaza Dr	San Diego, CA
Vons	Q00499	6155 El Cajon Blvd	San Diego, CA
Vons	Q00505	8310 Mira Mesa Blvd	San Diego, CA
Vons	Q00506	515 Washington St	San Diego, CA
Albertsons	Q00572	12475 Rancho Bernardo Rd	San Diego, CA
Vons	Q00576	7544 Girard Ave	San Diego, CA
Albertsons	Q00581	8650 Lake Murray Blvd	San Diego, CA
Vons	Q00592	4145 30th St	San Diego, CA
Vons	Q00615	4725 Clairemont Dr	San Diego, CA
Vons	Q00888	3550 Murphy Canyon Rd	San Diego, CA
Vons	Q00889	10675 Scripps Poway Pkwy	San Diego, CA
Lucky	Q00921	3457 McKee Rd	San Jose, CA
Safeway	Q01160	699 Lewelling Blvd	San Leandro, CA
Albertsons	Q00502	151 Woodland Pkwy	San Marcos, CA
Albertsons	Q00877	1929 W San Marcos Blvd	San Marcos, CA
Albertsons	Q01022	1571 San Elijo Rd	San Marcos, CA
Albertsons	Q00177	28090 S Western Ave	San Pedro, CA
Safeway	Q01039	11060 Bollinger Canyon Rd	San Ramon, CA
Food 4 Less	Q00320	2140 S Bristol St	Santa Ana, CA
Vons	Q00414	3650 S Bristol St	Santa Ana, CA
Albertsons	Q00487	27631 Bouquet Canyon Rd	Santa Clarita, CA
Safeway	Q00976	2751 4th St	Santa Rosa, CA
Vons	Q00504	2938 Tapo Canyon Rd	Simi Valley, CA
Albertsons	Q01218	543 Sweetwater Rd	Spring Valley, CA
Safeway	Q00975	6445 Pacific Ave	Stockton, CA
Safeway	Q01057	2808 Country Club Blvd	Stockton, CA
Vons	Q00507	2048 E Avenida de Los Arboles	Thousand Oaks, CA
Vons	Q00423	4705 Torrance Blvd	Torrance, CA
Vons	Q00706	24325 Crenshaw Blvd	Torrance, CA
Vons	Q00577	7789 Foothill Blvd	Tujunga, CA
Albertsons	Q00348	13270 Newport Ave	Tustin, CA
Safeway	Q00979	1790 Decoto Rd	Union City, CA
Albertsons	Q00661	1910 N Campus Ave	Upland, CA
Vons	Q00731	101 W Foothill Blvd	Upland, CA
Albertsons	Q00478	23850 Copperhill Dr	Valencia, CA
Albertsons	Q00488	1301 E Vista Way	Vista, CA
Albertsons	Q00516	1601 S Melrose Dr	Vista, CA
Safeway	Q00936	2800 Ygnacio Valley Rd	Walnut Creek, CA
Food 4 Less	Q00248	615 N Azusa Ave	West Covina, CA
Pavilions	Q00514	6534 Platt Ave	West Hills, CA
Pavilions	Q00415	8969 Santa Monica Blvd	West Hollywood, CA
Albertsons	Q00662	6755 Westminster Blvd	Westminster, CA
Vons	Q00327	15740 La Forge St	Whittier, CA
Vons	Q00243	20445 Yorba Linda Blvd	Yorba Linda, CA
Vons	Q00503	33644 Yucaipa Blvd	Yucaipa, CA
"""


rows = [line.split("\t") for line in data.strip().split("\n")]


csv_filename = "locations_CA.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(["Retailer", "Machine ID", "Address", "City"])

    writer.writerows(rows)

print(f"CSV file '{csv_filename}' created successfully!")