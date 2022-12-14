from ckiptagger import WS

path = "c:/users/Admin/anaconda3/envs/ckiptagger"
ws = WS(f"{path}/data")

text = '''曾任台積電共同營運長的蔣尚義，今年3月接受加州「電腦歷史博物館」（CHM）的口述歷史訪談時，透露他和台積電共同創辦人共事的祕訣，也說明張忠謀是怎麼聽簡報的。

這份近來公布的口述歷史訪談稿全文顯示，蔣尚義說，他在德州儀器工作約四年後，張忠謀在德州儀器的職位還比他高十階，但他也不認識張忠謀，就連台積電來延攬他時，他也還不認識張忠謀。

蔣尚義說，他加入台積電後，直接向張忠謀回報，而張忠謀對員工的期許很高。他說，他在台積電工作好幾年後，開始發現自己開始喝酒，而且工時非常長，因為家人不在台灣，他可能晚間9時、10時才回到家。

不過，他也開始發現張忠謀每天傍晚6時就回家，想當然耳，張忠謀的工作又更多，「我只負責研發，你還負責製造、銷售、行銷、政府關係、媒體和客戶，要關照所有事情，為什麼他能每天傍晚6時就回家」，因此他開始學習張忠謀的祕訣。

他說，若張忠謀要求下屬做簡報，期許會非常高，期望下屬告訴所屬領域最重要的事、而且是張忠謀不知道的事，下屬可能只有30分鐘的時間。

蔣尚義說，以他過去作為工程師的訓練，若在做簡報時從問題、實驗到方法全都交代，張忠謀完全沒耐心聽這些事，因此要反其道而行，先告訴張忠謀「這就是結果」，讓張忠謀覺得花這30分鐘值得，接著才有耐心聽細節，脾氣也很好，而且「非常、非常有耐心，他覺得他已經知道想知道的」。

若下屬不先講結果，「張忠謀會覺得浪費了5分鐘，接著還要浪費25分鐘，你會非常難過，他（張忠謀）會把你撕了，指責你、全程批評，他會撕掉報告，叫你出去」。

不過，蔣尚義是花了約四、五年的時間才理解這一點，但他會和其他同事分享和張忠謀共識的祕訣。

蔣尚義也透露他加入台積電也有一番曲折。他說，他是有一天在美西時間傍晚5時下班時，接到一個人的電話說，「我們有個研發副總裁職缺，希望你與我們共事，這是你的薪資、這是你的工作，這裡有筆簽約獎金」。他說，當時1987年成立的台積電已有十年歷史。

蔣尚義說，他當時回答，「不了，非常感謝，但我從沒想過回去台灣」，原因是當時他已經50歲了，台積電又是一家非常小的公司，可能不太穩定，他還有房貸和孩子的學費要繳，若在台積電的工作出狀況，接著很難找工作，但雙方之後又在談了半年後，他才孤身離開待了快30年的美國、回到台灣，家人則都留在美國。

他加入台積電的原因之一就在於，連絡他的人告知，簽約獎金是台積電的股票，他在簡單計算這筆股票的價值後，發現以他當時在惠普工作的薪資，若工作到65歲，所得還低於台積電股票的價值，基於財務誘因，他加入台積電，而且之後的薪酬又高上太多。'''

tokens = ws([text])[0]
print(tokens)