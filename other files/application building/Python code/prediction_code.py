from tensorflow.keras.utils import array_to_img

from tensorflow.keras.utils import img_to_array
from tensorflow import keras
model3=keras.models.load_model("train1.h5")
from tensorflow import keras
model4=keras.models.load_model("train2.h5")


def image_pred(i):
    i=img_to_array(i)
    i=np.expand_dims(i, axis=0)
    
    #________________views prediction________________
    
    result1= model3.predict(i)

    if result1[0][0]>result1[0][1]:
        if result1[0][2]>result1[0][0]:
            prediction="side image"
            class_views=2
        else:   
            prediction="front image"
            class_views=0
    else:
        prediction="rear image"
        class_views=1

    #__________________damage prediction______________________
    result2=model4.predict(i)

    if result2[0][0]>result2[0][1]:
        if result2[0][2]>result2[0][0]:
            predict="severe damage"
            class_damage=2
        else:   
            predict="mild damage"
            class_damage=1

    else:
        predict="low damage"
        class_damage=0

    return class_views,class_damage,prediction,predict


#function 2

#class_view{0:front,1:rear,2:side}
#class_damage(0:low,1:mild,2:high)

#function---depreciation and IDV
def calcidv(r,v,d):
    if(d==0):
        if(v==0):
            d_dep=0.5*r
            return d_dep
        elif(v==1):
            d_dep=0.07*r
            return d_dep
        else:
            d_dep=0.06*r
            return d_dep
    elif(d==1):
        if(v==0):
            d_dep=0.12*r
            return d_dep
        elif(v==0):
            d_dep=0.14*r
            return d_dep
        else:
            d_dep=0.15*r
            return d_dep
    elif(d==2):
        if(v==0):
            d_dep=0.17*r
            return d_dep
        elif(v==1):
            d_dep=0.18*r
            return d_dep
        else:
            d_dep=0.20*r
            return d_dep
    
    

#funtion------price           
def calculate(c,m,e,f):
    if(model=="tata" and m=="tiago"):
        price=649000
        return price
    else:
        if(f=="cng"):
            price=296661
            return price
        else:
            price=292667
            return price
    if(c=="renault" and m=="triber"):
        price=559000
        return price
    else:
        if(e==999):
            price=470990
            return price
        else:
            price=413290
            return price
    if(c=="dutsan" and m=="go"):
        price=528464
        return price
    else:
        if(e==999):
            price=43765
            return price
        else:
            price=351832
            return price
    if(c=="hyndai" and f=="cng"):
        price=547990
        return price
    else:
        price=503990
        return price
    return

#function-----premium amount calculator
def calculator(i):
    print("TOTAL PREMIUM AMOUNT:")
    own_damage=0.01970*i
    ncb_discount=0.2*own_damage
    od_premium=own_damage-ncb_discount
    net_premium=od_premium+100+50+1110
    gst=0.16*net_premium
    premium=gst+net_premium
    print("premium amount",premium)
    return premium

#main function


    
#----------mainfunction---------

#---------variables------------

def premium_prediction(name,contact_number,car_image,company_name,car_model,engine_capacity,fuel_type):
    n=name
    m=contact_number
    img=car_image
    cmp_name=company_name
    model=car_model
    engine=engine_capacity
    fuel=fuel_type
    #---------variables------------
    models=["tiago","nano_genx","triber","kwid","go","redi_go","santro"]
    dictc={"tata":("tiago","nano genx"),"renault":("triber","kwid"),"datsun":("go","redi_go"),"hyndai":("santro")}
    dengine={"tiago":("1199"),"nano":("624"), "kwid": ("999","799"), "triber":("999"), "go":("1198"),"redi":("999","799"),"santro":("1086")}
    #fuel type
    cng={"nano_genx","santro",""}
    class_views,class_damage,a,b=image_pred(img)
    verify=1
    if len(m)<10:
        verify=0
        msg="error!!!---contact number should be in 10 digit"
        return msg
    for i in m:
        if not(i>='0' and i<='9'):
            verify=0
            msg="error!!---enter valid contact number"
            return msg
            

    #-----------verfication--entered company and other details were real-----------------
    #----------function calling-----------------------
    if cmp_name in dictc.keys():
        l=list(dictc[cmp_name])
        verify+=1
        if model in l:
            if(dengine[model]=="kwid"):
                l_eng=list(dengine[model])
            else:
                l_eng=str(dengine[model])
            verify+=1
            if engine in l_eng:
                verify+=1
                if fuel_type=="cng":
                    if model in cng:
                        verify+=1
                        rate=str(calculate(cmp_name,model,engine,fuel_type))
                        loss=calcidv(rate,class_views,class_damage)
                        idv=rate-loss
                        premium=calculator(idv)

                else:
                    verify+=1
                    print("")
                    rate=calculate(cmp_name,model,engine,fuel_type)
                    loss=calcidv(rate,class_views,class_damage)
                    idv=rate-loss
                    premium=calculator(idv)
            else:
                msg="entered engine capacity not belongs to the car model--"+model+"\n__enter valid details"
        else:
            msg="entered car model not belongs to the company--"+cmp_name+"\n\nmodel available in this website---"+str(dictc[cmp_name])+"\n__enter valid details"
    else:
        msg="sorry!! <<<your car comany detail is not available>>>"
        
    if(verify==5):
        msg="VERIFIED"
        return ("customer name:  "+n+"\n"+"contact:  "+m+"\n"+msg+"...."+"\n\n----------------------------------------------------------------\n"
                +"\n"+"View of the car:  "+a+"\n "+"Damage level of the car:  "+b+"\n\n"+
                "Original price:  "+str(rate)+" \n"+"Depreciation rate:  "+str(loss)+"\n"+"IDV amount:  "+
                str(idv)+"\n"+"Premium amount:  "+str(premium))
    else:
        return(msg)
from tensorflow.keras.utils import load_img

