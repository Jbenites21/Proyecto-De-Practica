
# def prom(v1,v2,v3):
#     prom=(v1+v2+v3)/3;
#     return prom;

# def carga():
#     v1=int(input("ingrese un valor: "));
#     v2=int(input("ingrese un valor: "));
#     v3=int(input("ingrese un valor: "));
    
#     print("el promedio de",v1,v2,v3,"es",prom(v1,v2,v3));

# #main
# carga();


# def sup(l1,l2):
#     sup=l1*l2;
#     return sup;

# #main
# print("primer tirangulo");
# l1=int(input("ingrese un lado: "));
# l2=int(input("ingrese otro lado: "));
# print("segundo triangulo");
# l3=int(input("ingrese un lado: "));
# l4=int(input("ingrese otro lado: "));

# if sup(l1,l2)>sup(l3,l4):
#     print("el rectangulo uno tiene superficie mayor");
# else:
#     print("el triangulo dos tiene superficie mayor");
    

# def mult(list1,v1):
#     for f in range(5):
#         mult=list1[f]*v1;
#         print(list1[f],"*",v1,"=",mult);
    
# #main
# list1=[3,7,8,10,2];
# mult(list1,3);


# def carac(list1):
#     for f in range(len(list1)):
#         pos=0;
#         if len(list1[f])>len(list1[pos]):
#             pos=f;
#     return list1[f];

# #main
# list1=["enero","febrero", "marzo","abril"];
# print("la palabra con mas caracteres es:",carac(list1));


# def sueldos():
#     list1=[];
#     for f in range(10):
#         sueldo=int(input("ingrese un sueldo: "));
#         list1.append(sueldo);

#     return list1;

# def mayor(list1):
#     cont=0;
#     for f in range(len(list1)):
#         if list1[f]>4000:
#             cont=cont+1
#     return cont;

# def promedio(list1):
#     sum=0;
#     for f in range(len(list1)):
#         sum=sum+list1[f];
#     prom=sum/10;

#     return prom;

# def menor(list1):
#     prom=promedio(list1);
#     print("los sueldos menores al promedio son:");
#     for f in range(len(list1)):
#         if list1[f]<prom:
#             print(list1[f]);



# #main
# list1=sueldos();
# print(list1);
# print("=========================================================");
# print("hay",mayor(list1),"que tienen un sueldo mayor a 4000");
# print("=========================================================");
# print("el sueldo promedio es:",promedio(list1));
# print("=========================================================");
# menor(list1);


# def carga():
#     art=[];
#     val=[];

#     for f in range(5):
#         name=input("ingrese el nombre del producto: ");
#         art.append(name);
#         price=int(input("ingrese el precio: "));
#         val.append(price);

#     return [art,val];

# def mayor(art,val):
#     mayor=val[0];
#     pos=0;
#     for f in range(1,4):
#         if val[f]>mayor:
#             mayor=val[f];
#             pos=f;

#     print("el art con precio mayor es:",art[f]);  

# def menor(art,val):
#     men=int(input("ingrese un valor: "));
#     for f in range(5):
#         if val[f]<=men:
#             print(art[f]);               



# #main
# art,val=carga();
# print(art,val);
# mayor(art,val);
# menor(art,val);


# def tabla(valor,hasta=10):
#     #valor=int(input("ingres un valor: "));
#     for f in range(hasta):
#         mult=f*valor;
#         print(f,"*",valor,end="=");
#         print(mult);

# #main
# tabla(2,11);


# def carga():
#     list1=[];
#     for f in range(5):
#         nombre=input("ingrese un nombre: ");
#         s1=int(input("ingrese el primer sueldo: "));
#         s2=int(input("ingrese el segundo sueldo: "));
#         s3=int(input("ingrese el tercer sueldo: "));
#         list1.append([nombre,(s1,s2,s3)]);
#     return list1;

# def tot(list1):
#     for f in range(5):
#         total=list1[f][1][0]+list1[f][1][1]+list1[f][1][2];
#         print("el sueldo total de",list1[f][0],"es",total);
#         if total>10000:
#             print(list1[f][0],"tiene un sueldo myor a 10000");       

# def may(list1):
#     for f in range(5):
#         total=list1[f][1][0]+list1[f][1][1]+list1[f][1][2];
#         if total>10000:
#             print(list1[f][0],"tiene un sueldo myor a 10000");


# #main
# list1=carga();
# print(list1);
# print("=================================================");
# tot(list1);
# print("=================================================");
# may(list1);


def carga():
    list1=[];
    cand=int(input("ingrese la cantidad de candidatos: "));
    for f in range(cand):
        nombre=input("ingrese el nombre del candidato: ");
        cant1=int(input("ingrse la cantidad de ciudades: "));
        list2=[];
        for i in range(cant1):
            ciudad=input("ingrese la ciudad: ");
            cant=int(input("ingrese la cantidad de votantes: "));
            list2.append((ciudad,cant));
        list1.append((nombre,list2));

    return list1;

def mostrar(list1):
    for f in range(len(list1)):
        suma=0;
        for x in range(len(list1[f][1])):
            suma=suma+list1[f][1][x][1];

        print(list1[f][0],suma);
            


#main
list1=carga();
print(list1);
print("============================================");
mostrar(list1);



