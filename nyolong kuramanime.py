try:
    import os
    from requests_html import HTMLSession
    from clint.textui import progress
    import requests
except:
    import os
    os.system("pip install requests-html")
    os.system("pip install clint")
    os.system("pip install requests")

    

obes = HTMLSession()
ok = input("masukkan nama anime : ")
obs = []
obss =[]

folders=''
for i in __file__.split("\\")[0:len(__file__.split("\\"))-1]:
    folders = folders+i+'/'
    


oks = obes.get(f'https://kuramanime.pro/anime?order_by=latest&search={ok}&page=1')
for i in oks.html.xpath('/html/body/section/div/div/div/div/div/div/div/div/h5/a'):
    obs.append(i.attrs['href'])


print(f'di temukan {len(obs)} anime dengan keyword {ok}')
for ik in range(len(obs)):
    print(f"{ik+1}. {((obs[ik].split('/'))[5]).replace('-',' ')}")

okk = input("ingin mendownload yang mana : ")
olll = input("apakah anda ingin langsung mendowload semuanya (Y/n) : ")
opos = True    
opo = True
ikkk =1
session = HTMLSession()
if(not (os.path.exists(f"{folders}video"))):
    os.mkdir(f"{folders}video")
while (opos):
    opo = True
    while (opo):
        if (os.path.exists(f"{folders}video/{((obs[int(okk)-1].split('/'))[5]).replace('-',' ')} {ikkk}.mp4")):
            print(f"terskip bang si {((obs[int(okk)-1].split('/'))[5]).replace('-',' ')} {ikkk}")
            break
        ok = session.get(obs[int(okk)-1]+f'/episode/{ikkk}')
        # print(ok)
        if(ok.status_code == 404):
            print(f"kamu tersesat bang katanya, ga bisa deh download {((obs[int(okk)-1].split('/'))[5]).replace('-',' ')} eps {ikkk}")
            opos = False
            break
        
        
        elif (ok.status_code == 200):
            ok.html.render(sleep=1, keep_page=False, scrolldown =1, timeout=20)
            videos = ok.html.find('source')
            for il in videos:
                if (il.attrs['size'] == '720'):
                    obss.append(il.attrs['src'])
                    if(olll.upper() == 'Y'):
                        print(f"sedang mendownload {((obs[int(okk)-1].split('/'))[5]).replace('-',' ')} eps {ikkk} bang")
                        responsec = requests.get(il.attrs['src'], stream=True)
                        if(responsec.status_code != 200):
                            print('gagal download, sedang mencoba lagi')
                            break
                            
                        with open(f"{folders}video/{((obs[int(okk)-1].split('/'))[5]).replace('-',' ')} {ikkk}.mp4", 'wb') as f:
                            total_length = int(responsec.headers.get('content-length'))
                            for chunk in progress.bar(responsec.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                                if chunk:
                                    f.write(chunk)
                                    f.flush()
                        print()
                    else:
                        print(f'sedang mendapatkan link download nomor {ikkk}')
                    opo = False
    ikkk = ikkk+1
    


print('\n\n\n\n\n')
print(f"berikut link untuk mendownload anime {((obs[int(okk)-1].split('/'))[5]).replace('-',' ')}")
for i in range(len(obss)):
    print(f'{i+1}. {obss[i]}')
                    
