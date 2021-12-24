# カテゴリー
CATEGORIES = (
    ('0', 'AED設置箇所一覧'),
    ('1', '介護サービス事業所一覧'),
    ('2', '医療機器一覧'),
    ('3', '文化財一覧'),
    ('4', '観光施設一覧'),
    ('5', 'イベント一覧'),
    ('6', '公共無線LANアクセスポイント一覧'),
    ('7', '公衆トイレ一覧'),
    ('8', '消防水利施設一覧'),
    ('9', '指定緊急避難場所一覧'),
    ('10', '地域・年齢別人口'),
    ('11', '公共施設一覧'),
    ('12', '子育て施設一覧'),
)

# データセットカラム
DATASET = {
    # AED設置箇所一覧
    '0': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('名称', '名称'),
        ('名称_カナ', '名称_カナ'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('設置位置', '設置位置'),
        ('電話番号', '電話番号'),
        ('内線番号', '内線番号'),
        ('法人番号', '法人番号'),
        ('団体名', '団体名'),
        ('利用可能曜日', '利用可能曜日'),
        ('開始時間', '開始時間'),
        ('終了時間', '終了時間'),
        ('利用可能日時特記事項', '利用可能日時特記事項'),
        ('小児対応設備の有無', '小児対応設備の有無'),
        ('URL', 'URL'),
        ('備考', '備考'),
        ),

    # 介護サービス事業所一覧
    '1': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('介護サービス事業所名称', '介護サービス事業所名称'),
        ('介護サービス事業所名称_カナ', '介護サービス事業所名称_カナ'),
        ('実施サービス', '実施サービス'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('電話番号', '電話番号'),
        ('内線番号', '内線番号'),
        ('FAX番号', 'FAX番号'),
        ('法人番号', '法人番号'),
        ('法人の名称', '法人の名称'),
        ('事業所番号', '事業所番号'),
        ('利用可能曜日', '利用可能曜日'),
        ('利用可能曜日特記事項', '利用可能曜日特記事項'),
        ('定員', '定員'),
        ('URL', 'URL'),
        ('備考', '備考'),
        ),

    # 医療機器一覧
    '2': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('名称', '名称'),
        ('名称_カナ', '名称_カナ'),
        ('医療機関の種類', '医療機関の種類'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('電話番号', '電話番号'),
        ('内線番号', '内線番号'),
        ('FAX番号', 'FAX番号'),
        ('法人番号', '法人番号'),
        ('法人の名称', '法人の名称'),
        ('医療機関コード', '医療機関コード'),
        ('診療曜日', '診療曜日'),
        ('診療開始時間', '診療開始時間'),
        ('診療終了時間', '診療終了時間'),
        ('診療日時特記事項', '診療日時特記事項'),
        ('時間外における対応', '時間外における対応'),
        ('診療科目', '診療科目'),
        ('病床数', '病床数'),
        ('URL', 'URL'),
        ('備考', '備考'),
        ),

    # 文化財一覧
    '3': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('名称', '名称'),
        ('名称_カナ', '名称_カナ'),
        ('名称_通称', '名称_通称'),
        ('名称_英語', '名称_英語'),
        ('文化財分類', '文化財分類'),
        ('種類', '種類'),
        ('場所名称', '場所名称'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('電話番号', '電話番号'),
        ('内線番号', '内線番号'),
        ('員数（数）', '員数（数）'),
        ('員数（単位）', '員数（単位）'),
        ('法人番号', '法人番号'),
        ('所有者等', '所有者等'),
        ('文化財指定日', '文化財指定日'),
        ('利用可能曜日', '利用可能曜日'),
        ('開始時間', '開始時間'),
        ('終了時間', '終了時間'),
        ('利用可能日時特記事項', '利用可能日時特記事項'),
        ('画像', '画像'),
        ('画像_ライセンス', '画像_ライセンス'),
        ('概要', '概要'),
        ('概要_英語', '概要_英語'),
        ('説明', '説明'),
        ('説明_英語', '説明_英語'),
        ('URL', 'URL'),
        ('備考', '備考'),
        ),

    # 観光施設一覧
    '4': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('名称', '名称'),
        ('名称_カナ', '名称_カナ'),
        ('名称_英語', '名称_英語'),
        ('POIコード', 'POIコード'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('利用可能曜日', '利用可能曜日'),
        ('開始時間', '開始時間'),
        ('終了時間', '終了時間'),
        ('利用可能日時特記事項', '利用可能日時特記事項'),
        ('料金（基本）', '料金（基本）'),
        ('料金（詳細）', '料金（詳細）'),
        ('説明', '説明'),
        ('説明_英語', '説明_英語'),
        ('アクセス方法', 'アクセス方法'),
        ('駐車場情報', '駐車場情報'),
        ('バリアフリー情報', 'バリアフリー情報'),
        ('連絡先名称', '連絡先名称'),
        ('連絡先電話番号', '連絡先電話番号'),
        ('連絡先内線番号', '連絡先内線番号'),
        ('画像', '画像'),
        ('画像_ライセンス', '画像_ライセンス'),
        ('URL', 'URL'),
        ('備考', '備考'),
    ),

    # イベント一覧
    '5': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('イベント名', 'イベント名'),
        ('イベント名_カナ', 'イベント名_カナ'),
        ('イベント名_英語', 'イベント名_英語'),
        ('開始日', '開始日'),
        ('終了日', '終了日'),
        ('開始時間', '開始時間'),
        ('終了時間', '終了時間'),
        ('開始日時特記事項', '開始日時特記事項'),
        ('説明', '説明'),
        ('料金（基本）', '料金（基本）'),
        ('料金（詳細）', '料金（詳細）'),
        ('連絡先名称', '連絡先名称'),
        ('連絡先電話番号', '連絡先電話番号'),
        ('連絡先内線番号', '連絡先内線番号'),
        ('主催者', '主催者'),
        ('場所名称', '場所名称'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('アクセス方法', 'アクセス方法'),
        ('駐車場情報', '駐車場情報'),
        ('定員', '定員'),
        ('参加申込終了日', '参加申込終了日'),
        ('参加申込終了時間', '参加申込終了時間'),
        ('参加申込方法', '参加申込方法'),
        ('URL', 'URL'),
        ('備考', '備考'),
    ),

    # 公共無線LANアクセスポイント一覧
    '6': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('名称', '名称'),
        ('名称_カナ', '名称_カナ'),
        ('名称_英語', '名称_英語'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('設置者', '設置者'),
        ('電話番号', '電話番号'),
        ('内線番号', '内線番号'),
        ('SSID', 'SSID'),
        ('提供エリア', '提供エリア'),
        ('URL', 'URL'),
        ('備考', '備考'),
    ),

    # 公衆トイレ一覧
    '7': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('名称', '名称'),
        ('名称_カナ', '名称_カナ'),
        ('名称_英語', '名称_英語'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('設置位置', '設置位置'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('男性トイレ総数', '男性トイレ総数'),
        ('男性トイレ数（小便器）', '男性トイレ数（小便器）'),
        ('男性トイレ数（和式）', '男性トイレ数（和式）'),
        ('男性トイレ数（洋式）', '男性トイレ数（洋式）'),
        ('女性トイレ総数', '女性トイレ総数'),
        ('女性トイレ数（和式）', '女性トイレ数（和式）'),
        ('女性トイレ数（洋式）', '女性トイレ数（洋式）'),
        ('男女共用トイレ総数', '男女共用トイレ総数'),
        ('男女共用トイレ数（和式）', '男女共用トイレ数（和式）'),
        ('男女共用トイレ数（洋式）', '男女共用トイレ数（洋式）'),
        ('多機能トイレ数', '多機能トイレ数'),
        ('車椅子使用者用トイレ有無', '車椅子使用者用トイレ有無'),
        ('乳幼児用設備設置トイレ有無', '乳幼児用設備設置トイレ有無'),
        ('オストメイト設置トイレ有無', 'オストメイト設置トイレ有無'),
        ('利用開始時間', '利用開始時間'),
        ('利用終了時間', '利用終了時間'),
        ('利用可能時間特記事項', '利用可能時間特記事項'),
        ('画像', '画像'),
        ('画像_ライセンス', '画像_ライセンス'),
        ('備考', '備考'),
    ),

    # 消防水利施設一覧
    '8': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('種別', '種別'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('口径', '口径'),
        ('備考', '備考'),
    ),

    # 指定緊急避難場所一覧
    '9': (
        ('NotUse', '選択して下さい'),
        ('NO', 'NO'),
        ('名称', '名称'),
        ('名称_カナ', '名称_カナ'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('標高', '標高'),
        ('電話番号', '電話番号'),
        ('内線番号', '内線番号'),
        ('市区町村コード', '市区町村コード'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('災害種別_洪水', '災害種別_洪水'),
        ('災害種別_崖崩れ、土石流及び地滑り', '災害種別_崖崩れ、土石流及び地滑り'),
        ('災害種別_高潮', '災害種別_高潮'),
        ('災害種別_地震', '災害種別_地震'),
        ('災害種別_津波', '災害種別_津波'),
        ('災害種別_大規模な火事', '災害種別_大規模な火事'),
        ('災害種別_内水氾濫', '災害種別_内水氾濫'),
        ('災害種別_火山現象', '災害種別_火山現象'),
        ('指定避難所との重複', '指定避難所との重複'),
        ('想定収容人数', '想定収容人数'),
        ('対象となる町会・自治会', '対象となる町会・自治会'),
        ('URL', 'URL'),
        ('備考', '備考'),
    ),

    # 地域・年齢別人口
    '10': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('地域コード', '地域コード'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('調査年月日', '調査年月日'),
        ('地域名', '地域名'),
        ('総人口', '総人口'),
        ('男性', '男性'),
        ('女性', '女性'),
        ('0-4歳の男性', '0-4歳の男性'),
        ('0-4歳の女性', '0-4歳の女性'),
        ('5-9歳の男性', '5-9歳の男性'),
        ('5-9歳の女性', '5-9歳の女性'),
        ('10-14歳の男性', '10-14歳の男性'),
        ('10-14歳の女性', '10-14歳の女性'),
        ('15-19歳の男性', '15-19歳の男性'),
        ('15-19歳の女性', '15-19歳の女性'),
        ('20-24歳の男性', '20-24歳の男性'),
        ('20-24歳の女性', '20-24歳の女性'),
        ('25-29歳の男性', '25-29歳の男性'),
        ('25-29歳の女性', '25-29歳の女性'),
        ('30-34歳の男性', '30-34歳の男性'),
        ('30-34歳の女性', '30-34歳の女性'),
        ('35-39歳の男性', '35-39歳の男性'),
        ('35-39歳の女性', '35-39歳の女性'),
        ('40-44歳の男性', '40-44歳の男性'),
        ('40-44歳の女性', '40-44歳の女性'),
        ('45-49歳の男性', '45-49歳の男性'),
        ('45-49歳の女性', '45-49歳の女性'),
        ('50-54歳の男性', '50-54歳の男性'),
        ('50-54歳の女性', '50-54歳の女性'),
        ('55-59歳の男性', '55-59歳の男性'),
        ('55-59歳の女性', '55-59歳の女性'),
        ('60-64歳の男性', '60-64歳の男性'),
        ('60-64歳の女性', '60-64歳の女性'),
        ('65-69歳の男性', '65-69歳の男性'),
        ('65-69歳の女性', '65-69歳の女性'),
        ('70-74歳の男性', '70-74歳の男性'),
        ('70-74歳の女性', '70-74歳の女性'),
        ('75-79歳の男性', '75-79歳の男性'),
        ('75-79歳の女性', '75-79歳の女性'),
        ('80-84歳の男性', '80-84歳の男性'),
        ('80-84歳の女性', '80-84歳の女性'),
        ('85歳以上の男性', '85歳以上の男性'),
        ('85歳以上の女性', '85歳以上の女性'),
        ('世帯数', '世帯数'),
        ('備考', '備考'),
    ),

    # 公共施設一覧
    '11': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('名称', '名称'),
        ('名称_カナ', '名称_カナ'),
        ('名称_通称', '名称_通称'),
        ('POIコード', 'POIコード'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('電話番号', '電話番号'),
        ('内線番号', '内線番号'),
        ('法人番号', '法人番号'),
        ('団体名', '団体名'),
        ('利用可能曜日', '利用可能曜日'),
        ('開始時間', '開始時間'),
        ('終了時間', '終了時間'),
        ('利用可能日時特記事項', '利用可能日時特記事項'),
        ('説明', '説明'),
        ('バリアフリー情報', 'バリアフリー情報'),
        ('URL', 'URL'),
        ('備考', '備考'),
    ),

    # 子育て施設一覧
    '12': (
        ('NotUse', '選択して下さい'),
        ('都道府県コード又は市区町村コード', '都道府県コード又は市区町村コード'),
        ('NO', 'NO'),
        ('都道府県名', '都道府県名'),
        ('市区町村名', '市区町村名'),
        ('名称', '名称'),
        ('名称_カナ', '名称_カナ'),
        ('種別', '種別'),
        ('住所', '住所'),
        ('方書', '方書'),
        ('緯度', '緯度'),
        ('経度', '経度'),
        ('アクセス方法', 'アクセス方法'),
        ('駐車場情報', '駐車場情報'),
        ('電話番号', '電話番号'),
        ('内線番号', '内線番号'),
        ('FAX番号', 'FAX番号'),
        ('法人番号', '法人番号'),
        ('団体名', '団体名'),
        ('認可等年月日', '認可等年月日'),
        ('収容定員', '収容定員'),
        ('受入年齢', '受入年齢'),
        ('利用可能曜日', '利用可能曜日'),
        ('開始時間', '開始時間'),
        ('終了時間', '終了時間'),
        ('利用可能日時特記事項', '利用可能日時特記事項'),
        ('一時預かりの有無', '一時預かりの有無'),
        ('URL', 'URL'),
        ('備考', '備考'),
    ),
}

DATASET_COL = {
    # AED設置箇所一覧
    '0': ['都道府県コード又は市区町村コード',
          'NO',
          '都道府県名',
          '市区町村名',
          '名称',
          '名称_カナ',
          '住所',
          '方書',
          '緯度',
          '経度',
          '設置位置',
          '電話番号',
          '内線番号',
          '法人番号',
          '団体名',
          '利用可能曜日',
          '開始時間',
          '終了時間',
          '利用可能日時特記事項',
          '小児対応設備の有無',
          'URL',
          '備考'],

    # 介護サービス事業所一覧
    '1': ['都道府県コード又は市区町村コード',
          'NO',
          '都道府県名',
          '市区町村名',
          '介護サービス事業所名称',
          '介護サービス事業所名称_カナ',
          '実施サービス',
          '住所',
          '方書',
          '緯度',
          '経度',
          '電話番号',
          '内線番号',
          'FAX番号',
          '法人番号',
          '法人の名称',
          '事業所番号',
          '利用可能曜日',
          '利用可能曜日特記事項',
          '定員',
          'URL',
          '備考'],

    # 医療機関一覧
    '2': ['都道府県コード又は市区町村コード',
          'NO',
          '都道府県名',
          '市区町村名',
          '名称',
          '名称_カナ',
          '医療機関の種類',
          '住所',
          '方書',
          '緯度',
          '経度',
          '電話番号',
          '内線番号',
          'FAX番号'
          '法人番号',
          '法人の名称',
          '医療機関コード',
          '診療曜日',
          '診療開始時間',
          '診療終了時間',
          '診療日時特記事項',
          '時間外における対応',
          '診療科目',
          '病床数',
          'URL',
          '備考'],

    # 文化財一覧
    '3': ['都道府県コード又は市区町村コード',
          'NO',
          '都道府県名',
          '市区町村名',
          '名称',
          '名称_カナ',
          '名称_通称',
          '名称_英語',
          '文化財分類',
          '種類',
          '場所名称',
          '住所',
          '方書',
          '緯度',
          '経度',
          '電話番号',
          '内線番号',
          '員数（数）'
          '員数（単位）',
          '法人番号',
          '所有者等',
          '文化財指定日',
          '利用可能曜日',
          '開始時間',
          '終了時間',
          '利用可能日時特記事項',
          '画像',
          '画像_ライセンス',
          '概要',
          '概要_英語',
          '説明',
          '説明_英語',
          'URL',
          '備考'],

    # 観光施設一覧
    '4': ['都道府県コード又は市区町村コード',
          'NO',
          '都道府県名',
          '市区町村名',
          '名称',
          '名称_カナ',
          '名称_英語',
          'POIコード',
          '住所',
          '方書',
          '緯度',
          '経度',
          '利用可能曜日',
          '開始時間',
          '終了時間',
          '利用可能日時特記事項',
          '料金(基本)',
          '料金(詳細)',
          '説明',
          '説明_英語',
          'アクセス方法',
          '駐車場情報',
          'バリアフリー情報',
          '連絡先名称',
          '連絡先電話番号',
          '連絡先内線番号',
          '画像',
          '画像_ライセンス',
          'URL',
          '備考'],

    # イベント一覧
    '5': ['都道府県コード又は市区町村コード',
          'NO',
          '都道府県名',
          '市区町村名',
          'イベント名',
          'イベント名_カナ',
          'イベント名_英語',
          '開始日',
          '終了日',
          '開始時間',
          '終了時間',
          '開始日時特記事項',
          '説明',
          '料金(基本)',
          '料金(詳細)',
          '連絡先名称',
          '連絡先電話番号',
          '連絡先内線番号',
          '主催者',
          '場所名称',
          '住所',
          '方書',
          '緯度',
          '経度',
          'アクセス方法',
          '駐車場情報',
          '定員',
          '参加申込終了日',
          '参加申込終了時間',
          '参加申込方法',
          'URL',
          '備考'],

    # 公衆無線LANアクセスポイント一覧
    '6': ['都道府県コード又は市区町村コード',
          'NO',
          '都道府県名',
          '市区町村名',
          '名称',
          '名称_カナ',
          '名称_英語',
          '住所',
          '方書',
          '緯度',
          '経度',
          '設置者',
          '電話番号',
          '内線番号',
          'SSID',
          '提供エリア',
          'URL',
          '備考'],

    # 公衆トイレ一覧
    '7': ['都道府県コード又は市区町村コード',
          'NO',
          '都道府県名',
          '市区町村名',
          '名称',
          '名称_カナ',
          '名称_英語',
          '住所',
          '方書',
          '設置位置',
          '緯度',
          '経度',
          '男性トイレ総数',
          '男性トイレ数（小便器）',
          '男性トイレ数（和式）',
          '男性トイレ数（洋式）',
          '女性トイレ総数',
          '女性トイレ数（和式）',
          '女性トイレ数（洋式）',
          '男女共用トイレ総数',
          '男女共用トイレ数（和式）',
          '男女共用トイレ数（洋式）',
          '多機能トイレ数',
          '車椅子使用者用トイレ有無',
          '乳幼児用設備設置トイレ有無',
          'オストメイト設置トイレ有無',
          '利用開始時間',
          '利用終了時間',
          '利用可能時間特記事項',
          '画像',
          '画像_ライセンス',
          '備考'],

    # 消防水利施設一覧
    '8': ['都道府県コード又は市区町村コード',
          'NO',
          '都道府県名',
          '市区町村名',
          '種別',
          '住所',
          '方書',
          '緯度',
          '経度',
          '口径',
          '備考'],

    # 指定緊急避難施設一覧
    '9': ['NO',
          '名称',
          '名称_カナ',
          '住所',
          '方書',
          '緯度',
          '経度',
          '標高',
          '電話番号',
          '内線番号',
          '市区町村コード',
          '都道府県名',
          '市区町村名',
          '災害種別_洪水',
          '災害種別_崖崩れ、土石流及び地滑り',
          '災害種別_高潮',
          '災害種別_地震',
          '災害種別_津波',
          '災害種別_大規模な火事',
          '災害種別_内水氾濫',
          '災害種別_火山現象',
          '指定避難所との重複',
          '想定収容人数',
          '対象となる町会・自治会',
          'URL',
          '備考'],
    # 地域・年齢別人口
    '10': ['都道府県コード又は市区町村コード',
           '地域コード',
           '都道府県名',
           '市区町村名',
           '調査年月日',
           '地域名',
           '総人口',
           '男性',
           '女性',
           '0-4歳の男性',
           '0-4歳の女性',
           '5-9歳の男性',
           '5-9歳の女性',
           '10-14歳の男性',
           '10-14歳の女性',
           '15-19歳の男性',
           '15-19歳の女性',
           '20-24歳の男性',
           '20-24歳の女性',
           '25-29歳の男性',
           '25-29歳の女性',
           '30-34歳の男性',
           '30-34歳の女性',
           '35-39歳の男性',
           '35-39歳の女性',
           '40-44歳の男性',
           '40-44歳の女性',
           '45-49歳の男性',
           '45-49歳の女性',
           '50-54歳の男性',
           '50-54歳の女性',
           '55-59歳の男性',
           '55-59歳の女性',
           '60-64歳の男性',
           '60-64歳の女性',
           '65-69歳の男性',
           '65-69歳の女性',
           '70-74歳の男性',
           '70-74歳の女性',
           '75-79歳の男性',
           '75-79歳の女性',
           '80-84歳の男性',
           '80-84歳の女性',
           '85歳以上の男性',
           '85歳以上の女性',
           '世帯数',
           '備考'],

    # 公共施設一覧
    '11': ['都道府県コード又は市区町村コード',
           'NO',
           '都道府県名',
           '市区町村名',
           '名称',
           '名称_カナ',
           '名称_通称',
           'POIコード',
           '住所',
           '方書',
           '緯度',
           '経度',
           '電話番号',
           '内線番号',
           '法人番号',
           '団体名',
           '利用可能曜日',
           '開始時間',
           '終了時間',
           '利用可能日時特記事項',
           '説明',
           'バリアフリー情報',
           'URL',
           '備考'],

    # 子育て施設一覧
    '12': ['都道府県コード又は市区町村コード',
           'NO',
           '都道府県名',
           '市区町村名',
           '名称',
           '名称_カナ',
           '種別',
           '住所',
           '方書',
           '緯度',
           '経度',
           'アクセス方法',
           '駐車場情報',
           '電話番号',
           '内線番号',
           'FAX番号',
           '法人番号',
           '団体名',
           '認可等年月日',
           '収容定員',
           '受入年齢',
           '利用可能曜日',
           '開始時間',
           '終了時間',
           '利用可能日時特記事項',
           '一時預かりの有無',
           'URL',
           '備考'],
}
