

clear all
dt=1; 
delta=dt;
d=3;
load DJIA2013.dat
ndat1=fix(size(DJIA2013,1))
Y0=0;
Yfinal=ndat1;
 Y=DJIA2013(Y0+1:Yfinal,1);
 ndat=fix(size(Y,1));
     T1=Y0+1:Y0+ndat;
    Ygraf=Y(1:ndat,1);
    figure
    plot(T1,Ygraf(1:ndat,1))
    pause    

%M=fix(1800);
Tk=25;
nModel=ndat-Tk-d; 
Nc=56;
% matriz W
W=zeros(nModel,Nc);
k=delta/dt;

for i=1:d
    for j=1:nModel
        v(i,j)=Y(j +(d-1) - (i-1)*k,1);
    end
end
for j=1:nModel
    W(j,1)=1;
    for i=1:d
        W(j,i+1)=v(i,j);
    end
    % dobles prod
    col=d+2;
    for i1=1:d
        for i2=i1:d
            
            W(j,col)=v(i1,j)*v(i2,j);
            col=col+1;
        end
    end    
    % triples prod
        for i1=1:d
        for i2=i1:d
            for i3=i2:d
            
            W(j,col)=v(i1,j)*v(i2,j)*v(i3,j);
            col=col+1;
        end
        end
     end
          
     for i1=1:d
        for i2=i1:d
            for i3=i2:d
            for i4=i3:d
            W(j,col)=v(i1,j)*v(i2,j)*v(i3,j)*v(i4,j);
            col=col+1;
        end
        end
     end
 end
 
  for i1=1:d
        for i2=i1:d
            for i3=i2:d
            for i4=i3:d
                for i5=i4:d
            W(j,col)=v(i1,j)*v(i2,j)*v(i3,j)*v(i4,j)*v(i5,j);
            col=col+1;
                end
            end
            end
        end
    end
    vT(j)=Y(j+(d-1)+Tk);      
end    
    
  a=vT*pinv(W')  ;
 
'para modelar uso cantidad' 
nModel
  'intervalo, entre'
  Y0+1
  'hasta'
  Y0+nModel
   
  % prediccion
  %M=fix(ndat-Tk);
  nPre=ndat - d
  'para predecir uso cantidad' 
   nPre 
  'intervalo, entre'
  Y0+1
  'hasta'
  Y0+nPre
  % PREDICCION  
  for i=1:d
    for j=1:nPre
        v(i,j)=Y(j +(d-1) - (i-1)*k,1);
    end
end
for j=1:nPre
    W(j,1)=1;
    for i=1:d
        W(j,i+1)=v(i,j);
    end
    % dobles prod
    col=d+2;
    for i1=1:d
        for i2=i1:d            
            W(j,col)=v(i1,j)*v(i2,j);
            col=col+1;
        end
    end
    % triples prod
        for i1=1:d
        for i2=i1:d
            for i3=i2:d            
            W(j,col)=v(i1,j)*v(i2,j)*v(i3,j);
            col=col+1;
        end
        end
     end
     
     
     for i1=1:d
        for i2=i1:d
            for i3=i2:d
            for i4=i3:d
            W(j,col)=v(i1,j)*v(i2,j)*v(i3,j)*v(i4,j);
            col=col+1;
        end
        end
     end
 end
 
 
    for i1=1:d
        for i2=i1:d
            for i3=i2:d
            for i4=i3:d
                for i5=i4:d
            W(j,col)=v(i1,j)*v(i2,j)*v(i3,j)*v(i4,j)*v(i5,j);
            col=col+1;
        end
        end
     end
 end
end  
end
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
  for j=1:nPre
  predi(j)=a*W (j,:)';
end
    
    
    T1=Y0+1:Y0+nPre;
    Y1=Y(1:nPre,1);
   figure
    plot(T1,Y1(1:nPre,1))
   %pause
   figure
   T1Pre=Y0+1+Tk:Y0+nPre+Tk;
    plot(T1Pre,predi')
    pause
    figure
    plot(T1,Y1(1:nPre,1),T1Pre,predi','r')
   