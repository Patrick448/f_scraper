"""
Request new pronunciation

post to https://forvo.com/notsatisfied/
{"f":"requestPronounciation",
"idWord":"7384033",
"idLang":"186"}

-----------------------------------------------------

Request to login

 login_data = {
                "login": login,
                "password": password,
                "remember":"on"
                "_CSRF_INDEX": csrf_index,
                "_CSRF_TOKEN": csrf_token}

-------------------------------------------------------

Request to add a word

data = {
            'word': text,
            'id_lang': id,
            'modify': 0,
            is_phrase: 1 or 0
        }

------------------------------------------------------------

word check response examples:

{"error":0,
"errorMsg":"",
"data":{
	"status":"ok",
	"exists":1,
	"existsMessage":"<a href=\'https://forvo.com/word/amor/\'>Amor</a> is already in Forvo in Asturian [ast], Basque [eu], Bosnian [bs], Catalan [ca], Changzhou [plig], Croatian [hr], English [en], Galician [gl], Gan Chinese [gan], German [de], Hebrew [he], Interlingua [ia], Italian [it], Korean [ko], Latin [la], Lombard [lmo], Occitan [oc], Piedmontese [pms], Polish [pl], Portuguese [pt], Romanian [ro], Serbian [sr], Spanish [es], Turkish [tr], Venetian [vec]",
	"isWord":1,
	"isPhrase":0,
	"idWord":"3552",
	"idPhrase":0,
	"langs":[
		{"idLang":"191","code":"ast","name":"Asturian","isPhrase":0},
		{"idLang":"43","code":"eu","name":"Basque","isPhrase":0},
		{"idLang":"23","code":"bs","name":"Bosnian","isPhrase":0},
		{"idLang":"24","code":"ca","name":"Catalan","isPhrase":0},
		{"idLang":"400","code":"plig","name":"Changzhou","isPhrase":1},
		{"idLang":"61","code":"hr","name":"Croatian","isPhrase":0},
		{"idLang":"39","code":"en","name":"English","isPhrase":0}
	],

	"suggestedLangs":[{"idLang":"133","code":"pt","name":"Portuguese"}],
	"currentLangsList":"Asturian, Basque, Bosnian, Catalan, Changzhou, Croatian, English, Galician, Gan Chinese, German, Hebrew, Interlingua, Italian, Korean, Latin, Lombard, Occitan, Piedmontese, Polish, Portuguese, Romanian, Serbian, Spanish, Turkish, Venetian","isPersonName":"1","invalidChars":"","correctedWord":""}}


{"error":0,"errorMsg":"","data":{"status":"ok","exists":1,"existsMessage":"<a href=\"https://forvo.com/word/%E4%B8%AD%E5%9B%BD/\">中国</a> is already in Forvo in Cantonese [yue], Gan Chinese [gan], Hakka [hak], Japanese [ja], Jin Chinese [cjy], Korean [ko], Mandarin Chinese [zh], Min Dong [cdo], Min Nan [nan], Pu-Xian Min [cpx], Wu Chinese [wuu], Xiang Chinese [hsn]","isWord":1,"isPhrase":0,"idWord":"2052","idPhrase":0,
"langs":[{"idLang":"188","code":"yue","name":"Cantonese","isPhrase":0},
{"idLang":"291","code":"gan","name":"Gan Chinese","isPhrase":0},
{"idLang":"210","code":"hak","name":"Hakka","isPhrase":0},
{"idLang":"76","code":"ja","name":"Japanese","isPhrase":0},
{"idLang":"256","code":"cjy","name":"Jin Chinese","isPhrase":0},
{"idLang":"86","code":"ko","name":"Korean","isPhrase":1},
{"idLang":"186","code":"zh","name":"Mandarin Chinese","isPhrase":0},
{"idLang":"312","code":"cdo","name":"Min Dong","isPhrase":0},{"idLang":"197","code":"nan","name":"Min Nan","isPhrase":0},{"idLang":"401","code":"cpx","name":"Pu-Xian Min","isPhrase":0},{"idLang":"200","code":"wuu","name":"Wu Chinese","isPhrase":0},{"idLang":"261","code":"hsn","name":"Xiang Chinese","isPhrase":0}],"suggestedLangs":[{"idLang":"186","code":"zh","name":"Mandarin Chinese"},{"idLang":"188","code":"yue","name":"Cantonese"},{"idLang":"291","code":"gan","name":"Gan Chinese"},{"idLang":"256","code":"cjy","name":"Jin Chinese"},{"idLang":"200","code":"wuu","name":"Wu Chinese"},{"idLang":"261","code":"hsn","name":"Xiang Chinese"},{"idLang":"210","code":"hak","name":"Hakka"},{"idLang":"312","code":"cdo","name":"Min Dong"},{"idLang":"197","code":"nan","name":"Min Nan"}],"currentLangsList":"Cantonese, Gan Chinese, Hakka, Japanese, Jin Chinese, Korean, Mandarin Chinese, Min Dong, Min Nan, Pu-Xian Min, Wu Chinese, Xiang Chinese","isPersonName":"0","invalidChars":"","correctedWord":""}}
"""