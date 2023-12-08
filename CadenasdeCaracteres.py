
# cont1=0;
# x=0;
# oracion=input("ingrese una oracion: ");

# while x<len(oracion):
#     if oracion[x]==" ":
#         cont1=cont1+1;

#     x=x+1;

# print("tiene "+str(cont1)+" espacios");


# cont1=0;
# x=0;
# oracion=input("ingrese una oracion: ");
# oracion1=oracion.lower()

# while x<len(oracion1):
#     if oracion1[x]=="a" or oracion1[x]=="e" or oracion1[x]=="i" or oracion1[x]=="o" or oracion1[x]=="u":
#         cont1=cont1+1;
#     x=x+1;

# print("en la oracion ("+oracion1+") hay "+str(cont1)+" vocales");



# x="si";

# while x=="si":
#     clave=input("ingrese una contraseña de 10 a 20 caracteres: ");

#     if len(clave)>=10 and len(clave)<=20:
#         print("contraseña correcta");
#         x="no";
#     else:
#         print("contraseña incorrecta");


# list1=[101, 200, 20, 50, 99, 1000, 80, 2000];
# #x=0;
# con1=0;

# for x in range(len(list1)):
#     if list1[x]>100:
#         con1=con1+1;
#     #x=x+1;

# print("la lista",list1,"tiene",con1,"valores mayores a 100");


# list1=[];
# sum=0;
# prom=0;
# cont1=0;
# cont2=0;

# for f in range(5):
#     valor=float(input("ingrese una altura: "));
#     list1.append(valor);

#     sum=sum+list1[f];

# prom=sum//5;

# for f in range(5):
#     if list1[f]>prom:
#         cont1=cont1+1;
#     else:
#         cont2=cont2+1;


# print("la lista de alturas es",list1,"y tiene un promedio de",prom,"y hay",cont1,cont2,"personas mas altas y mas bajas al promedio respectivamente");


# list1=[];

# for f in range(5):
#     nombre=input("ingrese un nombre: ");
#     list1.append(nombre);

# menor=list1[0];

# for f in range(1,5):
#     if list1[f]<menor:
#         menor=list1[f];

# print("la persona menor en orden alfabetico es:",menor);


# list1=[];
# cont1=0;

# for f in range(5):
#     valor=int(input("ingrese un valor: "));
#     list1.append(valor);

# mayor=list1[0];

# for f in range(1,5):
#     if list1[f]>mayor:
#         mayor=list1[f];

# for f in range(5):
#     if list1[f]==mayor:
#         cont1=cont1+1;


# print("de la lista",list1,"el valor mayor es:",mayor,"y se repite:",cont1);0


# list1=[];
# list2=[];
# cont1=0;

# for f in range(5):
#     prod=input("ingrese un producto: ");
#     list1.append(prod);
#     prec=int(input("ingrese el precio:"));
#     list2.append(prec);

# menor=list2[0];

# for f in range(1,5):
#     if list2[f]>menor:
#         cont1=cont1+1;

# print("de la lista de productos",list1,"con precios",list2,"hay",cont1,"productos con precios mayores al primer producto")


# list1=[];
# list2=[];
# cont1=0;
# cont2=0;
# cont3=0;

# for f in range(4):
#     almn=input("ingrese un alumno: ");
#     list1.append(almn);
#     nota=int(input("ingrese la nota del alumno: "));
#     list2.append(nota);

# for f in range(4):
#     if list2[f]>=8:
#         cont1=cont1+1;

# print("hay",cont1,"con notas muy buenas")


# list1=[];
# list2=[];
# list3=[]

# for f in range (4):
#     valor1=int(input("ingre un valor de la primera lsita:" ));
#     list1.append(valor1);
#     valor2=int(input("ingrese un valor de la segunda lista: "));
#     list2.append(valor2);

# for f in range(4):
#     sum=list1[f]+list2[f];
#     list3.append(sum);

# print(list3);


# list1=[];

# for f in range(5):
#     nom=input("ingrese un nombre de un pais: ");
#     list1.append(nom);

# for x in range(4):
#     for f in range(4):
#         if list1[f]>list1[f+1]:
#             aux=list1[f];
#             list1[f]=list1[f+1];
#             list1[f+1]=aux;

# print(list1)

# for x in range(4):
#     for f in range(4):
#         if list1[f]<list1[f+1]:
#             aux=list1[f];
#             list1[f]=list1[f+1];
#             list1[f+1]=aux;

# print(list1)


# list1=[];
# list2=[];

# for f in range(5):
#     nom=input("ingrese el nombre del pais: ");
#     hab=int(input("ingrese la poblacion: "));
#     list1.append(nom);
#     list2.append(hab);

# for f in range(5):
#     print(list1[f],list2[f]);

# for x in range(4):
#     for f in range(4):
#         if list1[f]>list1[f+1]:
#             aux=list1[f];
#             list1[f]=list1[f+1];
#             list1[f+1]=aux;

# for x in range(4):
#     for f in range(4):
#         if list2[f]>list2[f+1]:
#             aux=list2[f];
#             list2[f]=list2[f+1];
#             list2[f+1]=aux;

# for f in range(5):
#     print(list1[f],list2[f]);


# list1=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]];

# for f in range(len(list1)):
#     for x in range(len(list1[f])):
#          if list1[f][x]>10:
#             list1[f][x]=0;


# print(list1);


# list2=[[1,2,3],[4,5,6],[0]];

# print(list2[len(list2)-1]);


# list1=[];
# list2=[];
# list3=[];

# for x in range(4):
#     pais=input("ingresse el nombre de un pais: ");
#     list1.append(pais);
#     temp1=int(input("ingrese una temperatura: "));
#     temp2=int(input("ingrese una temperatura: "));
#     temp3=int(input("ingrese una temperatura: "));
#     list2.append([temp1, temp2, temp3]);

# for f in range(4):
#     print(list1[f],list2[f]);

# print("===============================================================");

# for f in range(4):
#     sum=(list2[f][0]+list2[f][1]+list2[f][2])/3;
#     list3.append(sum);

# for f in range(4):
#     print(list1[f],list3[f]);

# print("===============================================================");

# pos=0;
# mayor=list3[0];

# for f in range(1,3):
#     if list3[f]>mayor:
#         mayor=list3[f];
#         pos=x;

# print("el pais con una temperatura media mayor es",list1[pos],"con una temperatura de:",mayor);


# list1=[];
# list2=[];

# for f in range(3):
#     nom=input("ingrese un nombre: ");
#     list1.append(nom);
#     cant=int(input("cuantos dias falto: "));
#     list2.append([]);
#     for x in range(cant):
#         dia=int(input("ingrese el dia que falto: "));
#         list2[f].append(dia);

# for f in range(3):
#     print(list1[f],"falto los dias",list2[f]);


# for f in range(3):
#     print(list1[f],"falto",len(list2[f]),"dias");

# menor=len(list2[0]);
# for f in range(1,3):
#     if len(list2[f])<menor:
#         menor=list2[f];

# for f in range(3):
#     if len(list2[f])==menor:
#         print(list1[f]); 


# list1=[];
# cont=1;

# for f in range(50):
#     list1.append([])
#     valor=1;
#     for x in range(cont):
#         list1[f].append(valor);
#         valor=valor+1;
#     cont=cont+1;

# print(list1);


# def cuadrado():
#     valor1=int(input("ingrese un valor: "));
#     cuad=valor1*valor1;
#     print(cuad);
#     print("==============================");

# def producto():
#     valor=int(input("ingrese un valor: "));
#     valor1=int(input("ingrese un valor: "));
#     prod=valor1*valor;
#     print(prod);

# #principal
# cuadrado();
# producto();

# def string(dato):
#     cont=0;
#     for x in range(len(dato)):
#         if dato[x]=="a" or dato[x]=="e" or dato[x]=="i" or dato[x]=="o" or dato[x]=="u":
#             cont=cont+1;

#     print(dato,"tiene",cont,"vocales");

# def carga():
#     nom=input("ingrese un nombre: ");
#     string(nom);


# #main
# for x in range(3):
#     carga();


# def mayor_menor(v1,v2,v3):
#     if v1<v2 and v1<v3:
#         if (v2<v3):
#             print(v1,v2,v3)
#         else:
#             print(v1,v3,v2)
#     else:
#         if (v2<v3):
#             if (v1<v3):
#                 print(v2,v1,v3)
#             else:
#                 print(v2,v3,v1)
#         else:
#             if (v1<v2):
#                 print(v3,v1,v2)
#             else:
#                 print(v3,v2,v1)

# def carga():
#     v1=int(input("ingrese un valor: "));
#     v2=int(input("ingrese un valor: "));
#     v3=int(input("ingrese un valor: "));
#     mayor_menor(v1,v2,v3);

# #main
# carga();







