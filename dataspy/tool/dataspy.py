# PROJETO DE FERRAMENTA FORENSE - DATASPY
# Idealizado e construido por K.r.s
# Github: https://github.com/IK-R-S
# protegido pela licença GNU GPLv3

from metadata_image import *

from time import sleep as s
from tinytag import TinyTag
from exif import Image
import vlc
import PIL.Image 
import os

os.system('clear')

print('iniciando DataSpy...')
s(1)
os.system('clear')
print(' ')
print('''\033[1;97m 
             `.--:--.                             
         `:ohdataspyhyo/.                         
       -oo/:::::::::/+syys-                       
     `os::::::::::::::::+yhs`                     
    .h+--::://///////:/:::sdh.                    
    sy:://///////////::/:::sdy`                   
   `ds////////////////://:::hh:                   
   `ds///////////////////:::oh:                   
    sh///////////////////:::oy.                   
    `hh///////////////::::::y/                    
     .yh+////::::::::::::::sy                     
       +hy+///::----:::::/sm+                     
        `:ohso+/::::://ohmNmms.                   
            -/+osssso/://:yNNmms.                 
                           r:dNNmmo`               
 ______           _           ______          
|_   _ `.        / |_       .' ____ \                  
  | | `. \ ,--. `| |-',--.  | (___ \_|_ .--.   _   __  
  | |  | |`'_\ : | | `'_\ :  _.____`.[ '/'`\ \[ \ [  ] 
 _| |_.' /// | |,| |,// | |,| \____) || \__/ | \ '/ /  
|______.' \'-;__/\__/\'-;__/ \______.'| ;.___/   \_:/   
                                      [_|       /_/              
                                      [ ]Nmmo` / /         
                                       dataspy '        
                                        ihNmm+ '       
                                          fgu5'     ''')                                          
print('v1.0 criada por K.r.s')
s(3)
os.system("clear") 
print(' ')
print('''
                                                                 
                                                                 
7MM"""Yb.            mm                                         
 MM    `Yb.          MM                                         
 MM     `Mb  ,6"Yb.mmMMmm  ,6"Yb.  ,pP"Ybd `7MMpdMAo.`7M'   `MF'
 MM      MM 8)   MM  MM   8)   MM  8I   `"   MM   `Wb  VA   ,V  
 MM     ,MP  ,pm9MM  MM    ,pm9MM  `YMMMa.   MM    M8   VA ,V   
 MM    ,dP' 8M   MM  MM   8M   MM  L.   I8   MM   ,AP    VVV    
JMMmmmdP'   `Moo9^Yo.`Mbmo`Moo9^Yo.M9mmmP'   MMbmmd'     ,V     
                                              MM         ,V      
                                            .JMML.    OOb"       
    ''')
print(' ')
print('           \033[1;30;107mimagens [i]  -  áudios [a]  -  sair [s]')

print('\033[0;0m ')
tool = 0
while tool != 's':
    print(' ')
    tool = str(input('\033[1;92m> Oque deseja analisar? [i][a][s]: \033[1;97m')).lower().strip()[0]

    #ANÁLISE DE IMAGENS:

    if tool == 'i':
      ok = 0
      while True:
        try:
            os.system('clear')
            print('\033[1;36mANÁLISE DE IMAGEM')
            print(' ')
            foto = str(input('\033[1;34m(sair[s]) > arraste o caminho do arquivo de imagem: \033[1;97m'))
            if foto == 's':
                print(' ')
                print('\033[1;91mCancelado.')
                s(1)
                break
            foto = foto.replace("'"," ")
            foto = foto.strip()
            os.system("clear")
            
            with open(foto,"rb") as f:
                img = Image(f)
                print('\033[1;31mMetadados da imagem')
                print(' ')
                print(f'\033[1;93mCAMINHO DO ARQUIVO: \033[1;32m {foto}\n')
                metadata_image() # Outro caminho

            print(' ')
            ver_imagem = ' '
            while ver_imagem not in 'sn':
                ver_imagem = str(input('\033[1;97mvisualizar a imagem? [s][n] >>> ')).strip().lower()[0]
            if ver_imagem == 's':
                visualizar = PIL.Image.open(foto)
                visualizar.show()
                print(' ')
                print('\033[1;95mIMAGEM CARREGADA DE {}'.format(foto))
            else:
                print('\033[1;91mvisualização negada.')
            ok = 1
            if ok == 1:
                break
        except:
            print('\033[1;31mErro ao analisar o arquivo de imagem. Tente novamente.')
            s(2)
        


    #ANALISE DE ÁUDIOS:
    
    elif tool == 'a':
        ok2 = 0
        while True:
            try:
                os.system('clear')
                print('\033[1;36mANÁLISE DE ÁUDIOS')
                print(' ')
                msc = input('\033[1;34m(sair[s]) > arraste o caminho do arquivo de áudio: \033[1;97m')
                if msc == 's':
                    print(' ')
                    print('\033[1;91mCancelado.')
                    s(1)
                    break
                os.system('clear')
                msc = msc.replace("'"," ")
                msc = msc.strip()
                tag = TinyTag.get(msc)
                
                print('\033[1;31mMetadados do áudio\n')
                print(f'\033[1;93mTÍTULO: \033[1;32m {tag.title}\n')
                print(f'\033[1;93mDURAÇÃO (segundos): \033[1;32m {tag.duration}\n')
                print(f'\033[1;93mÁLBUM: \033[1;32m {tag.album}\n')
                print(f'\033[1;93mÁLBUM (Artista): \033[1;32m {tag.albumartist}\n')
                print(f'\033[1;93mARTISTA: \033[1;32m {tag.artist}\n')
                print(f'\033[1;93mANO: \033[1;32m {tag.year}\n')
                print(f'\033[1;93mBYTES (antes da reprodução): \033[1;32m {tag.audio_offset}\n')
                print(f'\033[1;93mTAXA DE BITS: \033[1;32m {tag.bitrate}\n')
                print(f'\033[1;93mCOMENTÁRIOS: \033[1;32m {tag.comment}\n')
                print(f'\033[1;93mCOMPOSITOR: \033[1;32m {tag.composer}\n')
                print(f'\033[1;93mNÚMERO DO DISCO: \033[1;32m {tag.disc}\n')
                print(f'\033[1;93mTOTAL DE DISCOS: \033[1;32m {tag.disc_total}\n')
                print(f'\033[1;93mTAMANHO DO ARQUIVO (bytes): \033[1;32m {tag.filesize}\n')
                print(f'\033[1;93mGÊNERO: \033[1;32m {tag.genre}\n')
                print(f'\033[1;93mAMOSTRAS POR SEGUNDO: \033[1;32m {tag.samplerate}\n')
                print(f'\033[1;93mFAIXA: \033[1;32m {tag.track}\n')
                print(f'\033[1;93mTOTAL DE FAIXAS: \033[1;32m {tag.track_total}\n')
                escutar_som = ' '
                while escutar_som not in 'sn':
                    escutar_som = str(input('\033[1;97mescutar o áudio? [s][n] >>> ')).strip().lower()[0]
                    if escutar_som == 's':
                        som = vlc.MediaPlayer(msc)
                        som.play()
                        print(' ')
                        stop = str(input('\033[1;95m(parar[ENTER]) - TOCANDO ÁUDIO DE {}: \033[1;97m'.format(msc)))
                        som.stop()
                        print(' ')
                        print('\033[1;91máudio finalizado.')
                    else:
                        print('\033[1;91mvisualização negada.')


                ok2 = 1
                if ok2 == 1:
                    break
            except:
                print('\033[1;31mErro ao analisar o áudio. Tente novamente.')
            s(2)

os.system('clear')
print('\033[1;31m Dataspy finalizado')
s(1)
os.system('clear')
