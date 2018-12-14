
import os 


def transform_class(p_class):
    if(p_class=='1'):
        return 'pedestrian'
    elif (p_class=='2'):
        return 'people'
    elif (p_class=='3'):
        return 'bicycle'
    elif (p_class=='4'):
        return 'car'
    elif (p_class=='5'):
        return 'van'
    elif (p_class=='6'):
        return 'truck'
    elif (p_class=='7'):
        return 'tricycle'
    elif (p_class=='8'):
        return 'awning-tricycle'
    elif (p_class=='9'):
        return 'bus'
    elif (p_class=='10'):
        return 'motor'






root_path =  os.getcwd()
gt = root_path+'/ground-truth/'

for file in os.listdir(os.path.join(gt)):
	if not os.path.isdir(os.path.join(gt,file)):
		with open(os.path.join(gt,file)) as f:
			print(file)
			a = f.readlines()
			b =[]
			for line in a :
			    line = line.split(',')
			    line[0] = transform_class(line[0])                
			    line = ' '.join(b)
			    b.append(line)
			f.writelines(b)
			f.close()
