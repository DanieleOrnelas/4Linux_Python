import matplotlib
matplotlib.use('Agg')
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl
import pandas as pd
import datetime
from datetime import timedelta
print('Pacotes importados')

## Load do diretorio com os dados:
# os.chdir('/home/fazzt/teste_raio')
os.chdir('/home/fazzt/raios_web/data')

arqv=os.listdir()

##############################################################################################
##Load dos dados:
print('Importando e tratando os dados...')

### Importando os dados:
df = pd.read_csv(arqv[0],
                 sep="\s+", #separator whitespace
                 header=None)
df.columns=['data','horario', 'lat', 'lon', 'intensidade']

#Transformando as datas e horarios em lista de string:
data=df['data'].tolist()
hora=df['horario'].tolist()
#Variaveis numericas:
lat=df['lat'].values.tolist()
lon=df['lon'].values.tolist()
sinal=df['intensidade'].values.tolist()

####Organizacao dos dados:
occ=[]
mydate=[]
for i in range(len(data)):   
   dtstr=[]
   #mydate.append(datetime.datetime(int(data[i][0:4]), int(data[i][5:7]),\
    #int(data[i][8:10]), int(hora[i][0:2]), int(hora[i][3:5])))
   dtstr.append(int(data[i][0:4])) #Ano
   dtstr.append(int(data[i][5:7])) #Mes  
   dtstr.append(int(data[i][8:10])) #Dia
   #correcao do horario de UTC para GMT-3
   if int(data[i][5:7])==12 or int(data[i][5:7])<=2:
      h=int(hora[i][0:2])-2 #Hora dentro do horario de verao
   elif int(data[i][5:7])>2 and int(data[i][5:7])<=11:
      h=int(hora[i][0:2])-3 #Hora fora do horario de verao
   if h<=9:
      hr= '0' + str(h)
   elif h>=10:
      hr = str(h)
   dtstr.append(h)  #Horario com correcao
   dtstr.append(int(hora[i][3:5])) # Minutos
   dtstr.append(lat[i]) #Latitude
   dtstr.append(lon[i]) #Longitude
   dtstr.append(sinal[i]) #Intensidade KA
   dtstr.append(data[i]) #Data em string
   horario= hr  + ':' + hora[i][3:5] + ':' + hora[i][6:8]
   dtstr.append(horario) #Horario string
   mydate.append(datetime.datetime(int(data[i][0:4]), int(data[i][5:7]),\
    int(data[i][8:10]), int(hr), int(hora[i][3:5])))
   occ.append(dtstr)
## Limpando variaveis que nãserao mais utitlizadas:
#occ=np.array(occ)

print('Dados tratados e organizados!')
#Variavel occ sera a variavel a ser trabalha nos proximos passos.
##############################################################################################
### Para o loop, preciso saber o horario inicial e final dos dados
hi=int(occ[0][3]) #Hora Inicial
mi=int(occ[0][4]) #Minuto Inicial
hf=int(occ[-1][3]) #Hora Final
mf=int(occ[-1][4]) #Minuto Final
print('Hora Inicial --> %s:%s ; Hora Final --> %s:%s'%(hi,mi,hf,mf))

### Loop de uma hora:
# Os dados devem estar entre hf-1:mf e hf:mf
# Esta etapa pega os dados da ultima hora, separando as datas e horarios dessa ulltima hora
print('Gerando variaveis de descargas atmosfericas acumuladas por intervalos de tempo...')
print('Para o Loop de 1hr --> passo de tempo de 10 minutos.')
print('Para o Looop de 3hrs --> passo de tempo de 30 minutos.')

# Loop para os dois casos (1hr e 3 hr)
dp=[]
for i in range(0,2,1):
   if i==0: #condicoes para 1hr:
      d = mydate[-1] - datetime.timedelta(hours=1) #Primeiro registro de descargas na ultima hora
      #print(d)
      dt=10
      dp.append('dados da ultima 1hr')
      print('Seperando dados para as descargas ocorridas na ultima hora...')
   elif i==1:  #condicoes para 3hrs:
      d = mydate[0] #horario de registro da primeira descarga
      #print(d)
      dt=30
      dp.append('dados das ultimas  3hrs')
      print('Separando dados para as descargas ocorridas nas ultimas tres horas...')
   end_date=mydate[-1]
   delta = datetime.timedelta(minutes=dt)
   int_hrs=[]
   while d<=end_date:
     # print(d.strftime("%Y-%m-%d %H:%M"))
      int_hrs.append(d)
      d += delta
      #print(int_hrs)
   #Com os intervalos de tempo gerados, separo os dados que se enquadram nesses uintervalos:
   dscrg=[]
   for i in range(len(int_hrs)-1):
      dti=int_hrs[i]
      dtf=int_hrs[i+1] 
      dti=dti.strftime('%d/%m/%Y - %H:%M') 
      dtf=dtf.strftime('%d/%m/%Y - %H:%M') 
      dmy=dti[0:10]
      hri=dti[13:18]
      hrf=dtf[13:18]
      del(dti, dtf)
      dscrg.append('Descargas Atmosfericas detectadas no dia %s entre %s e %s' %(dmy, hri, hrf))
      dplt=[]
      for j in range(len(mydate)):
         if mydate[j]>=int_hrs[i] and mydate[j]<=int_hrs[i+1]:
#            print(mydate[j])
            dplt.append(occ[j])
      if len(dplt)==0:
         dscrg.append(dplt)
      elif len(dplt)!=0:
         dscrg.append(np.stack(dplt,axis=0))
   dp.append(dscrg)

print('Variavel "dp" criada. Estrutura da variavel:  dp[0]="Dados 1hr";  dp[1]=Dados da ultima hora em intervalor de 10 minutos;  dp[2]="Dados 3hrs";  dp[3]=Dados das ultimas tres horas em intervalos de 30 minutos')
print('Etapa finalizada, passando para o proximo passo...')

#################################################################################
### Preparando para o plot:
print('Realizando plot dos dados de decargas atmosfericas e criando gif dinamico')

for h in range(1,len(dp),2):
   print('Plot das descargas para os %s' %(dp[h-1]))
   varplot=dp[h]
   #Gerando escalas de cor de acorodo com o tempo de plot:
   varcount=[]
   for t in range(1,len(varplot),2):
      arqv=varplot[t]
      for l in arqv:
         varcount.append(l)
   print('Total de %s para o acumulado de %s' %(len(varcount), dp[h-1]))
   print('Total de %s passos de tempo'%(int(len(varplot)/2)))
   #Gerando os intervalos percentuais para a colorbar:
   cmap = plt.get_cmap('jet')
   indices = np.linspace(0, cmap.N, (len(varplot)/2))
   my_colors = [cmap(int(j)) for j in indices]
   k=0
   fig = plt.figure(figsize=(18,12))
   #Plot do mapa
   m = Basemap(projection='merc', llcrnrlon=-58, llcrnrlat=-27, urcrnrlon=-38, urcrnrlat=-7)
   parallels = np.arange(-5,-30,-2)
   m.drawparallels(parallels,labels=[True,False,False,True], fontsize=15, linewidth=1.5)
   meridians = np.arange(-60,-30,2)
   m.drawmeridians(meridians,labels=[True,False,False,True], fontsize=15, linewidth=1.5)
   m.bluemarble()
   #m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 1500, verbose= True) 
   # Load dos shapes --> Contorno dos paises e estados do Brasil
   m.readshapefile('/dados/backup_homefazzt/download/ne_10m_admin_0_countries','ne_10m_admin_0_countries',linewidth=1, color='white')
   m.readshapefile('/dados/backup_homefazzt/download/shape/Brasil_com_estados','estados_2010',linewidth=1,color='white')
   #Shapes - Furnas:
   m.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/138kV_2D','138kV',linewidth=1,color='#FF0000')
   m.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/230kV_2D','230kV',linewidth=1,color='#00FF09')
   m.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/345kV_2D','345kV',linewidth=1,color='#FFC400')
   m.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/500kV_2D','500kV',linewidth=1,color='#001AFF')
   m.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/600kV_2D','600kV',linewidth=1,color='#FF00EF')
   m.readshapefile('/dados/backup_homefazzt/download/KML_to_shape/750kV_2D','750kV',linewidth=1,color='#00FFFF')
   #Defininco as escalas de range da colorbar
   msc=[]
   for z in range(1, len(varplot),2):
       msc.append(len(varplot[z]))
   maxsc=max(msc)
   print(maxsc)
   for i in range(1,len(varplot),2):
      db=varplot[i]
      #Abre a figura para o plot
      #fig = plt.figure(figsize=(18,12))
      print('Gerando figura --> %s' %varplot[i-1])
      print(len(db))
      date_plot=varplot[i-1][41:51] #data em questao
      hr_plot=varplot[i-1][58:71] #intervalo hoarario em questao
      if h==1:
         plt.suptitle('Descargas Atmosféricas na última hora',  fontsize=18)
      elif h==3:
         plt.suptitle('Descargas Atmosféricas nas últimas três horas', fontsize=18)
      plt.title('Dia %s - entre %s' %(date_plot, hr_plot), fontsize=20)
      lon=[]
      lat=[]
      sgn=[]
      hrs=[]
      for j in range(np.shape(db)[0]):
         lon.append(np.float(db[j][6]))
         lat.append(np.float(db[j][5]))
         sgn.append(np.float(db[j][7]))
         hrs.append(db[j][9])
      x, y = m(lon, lat) 
      for cnt in range(len(lon)):
         if sgn[cnt]<0:
            mrkr='.'
            mkrs=12
         elif sgn[cnt]>0:
            mrkr='P'
            mkrs=12
         m.plot(x[cnt], y[cnt], mrkr, markersize=mkrs, color=my_colors[k])
     # Inserindo colorbar com os horarios indicados:
     #N_TICKS=6
     #indexes = [x for x in np.linspace(0,len(db)-1,N_TICKS).astype(int)]
     #ticks= [m for m in indexes] 
     #lbl=[]
     #for r in indexes:
     #   for c in range(len(db)): 
     #      if c==r:
     #         lbl.append(hrs[r])
      if i==1:
         norm = mpl.colors.Normalize(vmin=0, vmax=maxsc)
         sm = plt.cm.ScalarMappable(cmap=cmap,norm=norm)
         sm.set_array([])
         ticks=[0, maxsc] 
         cb=plt.colorbar(sm, ticks=ticks)
         cb.set_ticklabels(['Antigos', 'Recentes']) #lbl)
         cb.ax.tick_params(labelsize=15)
      #Abrindo diretorio em que as imagens serao salvas:
      if h==1 and i==1:
        os.chdir('/produtos/Raios_Web/img1hr')
        os.system('rm -rf *.png')
      elif h==3 and i==1:
         os.chdir('/produtos/Raios_Web/img3hr')
         os.system('rm -rf *.png')
      plt.savefig('img%s.png' %(k+1)) #salva figura
      
      if h==1 and i==len(varplot)-1: # Chegou na ultima imagem
         f = plt.gcf
         plt.suptitle('')
         plt.savefig('/produtos/Raios_Web/img1hr/acumulado/acumulado_ultima_hora.png')
      elif h==3 and i==len(varplot)-1:
         f = plt.gcf
         plt.suptitle('')
         plt.savefig('/produtos/Raios_Web/img3hr/acumulado/acumulado_3hrs_hora.png') 
      #plt.close()
      k+=1

   ### Sessao em que abre a pasta com as imagens e cria o gif por linha de comando no linux (image magik)
   file_list = glob.glob('*.png') # Get all the pngs in the current directory
   file_list=sorted(file_list)
   os.system('convert -delay 80 -loop 0 *.png descargas_teste.gif') # On windows convert is 'magick'
   print('Gif criado --> %s' %(dp[h-1]))


print('Importando e tratando os dados...')

