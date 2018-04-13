from lvq1 import lvq1
from lvq2 import lvq2
from lvq3 import lvq3
from lvq import lvq
from arquivo import arquivo

##database2 = [[1, 2, 'a'], [0.9, 2.2, 'a'], [0.1, 2.5, 'a'], [0, 0, 'b'], [1.5, 3, 'b']]

##database2 = [[1.1,1.4,1.4,1.4,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,2,2,2,2,1.2,1.2,1.2,1.2,1.4,'no'],[1,1.0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,'yes'],[415,59.0,50,51,1159,8411.31,0.01,103.53,81.24,870848.58,2.8,48380.48,359,35,9,10,47,106,692,467,106,'yes'],[230,33.0,10,16,575,3732.82,0.03,39.82,93.74,148644.06,1.24,8258,174,15,34,5,23,67,343,232,65,'yes'],[175,26.0,12,13,500,3123.96,0.03,29.48,105.96,92103.07,1.04,5116.84,142,7,19,4,18,58,310,190,51,'yes'],[163,16.0,13,11,440,2714.77,0.03,32.25,84.14,87589.65,0.9,4866.09,139,2,20,0,19,53,260,180,31,'yes'],[152,11.0,6,11,432,2629.78,0.03,31.68,83.01,83311.56,0.88,4628.42,114,18,17,0,18,50,256,176,21,'yes'],[3,1.0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,'no'],[14,2.0,1,2,22,88,0.17,5.79,15.21,509.14,0.03,28.29,8,0,1,0,9,7,13,9,3,'no'],[14,2.0,1,1,11,36.54,0.27,3.75,9.74,137.03,0.01,7.61,3,9,0,0,6,4,6,5,3,'no'],[10,2.0,1,2,18,64.53,0.14,7,9.22,451.71,0.02,25.09,8,0,0,0,8,4,11,7,3,'no'],[8,1.0,1,1,10,31.7,0.5,2,15.85,63.4,0.01,3.52,3,0,0,1,4,5,5,5,1,'no'],[6,1.0,1,1,5,11.61,0.67,1.5,7.74,17.41,0,0.97,2,0,2,0,3,2,3,2,1,'no'],[6,1.0,1,1,16,57.36,0.35,2.86,20.08,163.88,0.02,9.1,5,0,0,0,5,7,8,8,1,'no'],[2,1.0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,3,2,3,2,1,'no'],[2,1.0,1,1,5,11.61,0.67,1.5,7.74,17.41,0,0.97,0,0,0,0,1,0,1,0,1,'no'],[39,4.0,1,2,83,429.1,0.05,19,22.58,8152.97,0.14,452.94,29,1,7,0,19,17,49,34,7,'no'],[5,1.0,1,1,7,19.65,0.4,2.5,7.86,49.13,0.01,2.73,2,1,0,0,5,2,5,2,1,'no'],[9,2.0,1,1,21,87.57,0.25,4,21.89,350.27,0.03,19.46,8,0,0,0,8,10,11,10,3,'no'],[11,1.0,1,1,25,108.05,0.27,3.77,28.67,407.26,0.04,22.63,8,0,1,0,7,13,11,14,1,'no'],[63,10.0,4,5,157,829.81,0.05,18.2,45.59,15102.51,0.28,839.03,55,2,4,0,14,25,92,65,19,'no'],[74,12.0,4,5,193,1135.35,0.05,19.92,57,22614.95,0.38,1256.39,56,5,8,0,22,37,126,67,19,'no'],[10,1.0,1,1,17,53.89,0.5,2,26.94,107.78,0.02,5.99,5,0,0,0,3,8,9,8,1,'no'],[7,1.0,1,1,17,58.81,0.67,1.5,39.21,88.22,0.02,4.9,5,0,0,0,3,6,9,8,1,'no'],[4,1.0,1,1,9,25.27,0.67,1.5,16.84,37.9,0.01,2.11,2,0,0,0,3,4,5,4,1,'no'],[4,1.0,1,1,6,15.51,0.4,2.5,6.2,38.77,0.01,2.15,2,0,0,0,5,1,5,1,1,'no'],[5,1.0,1,1,5,11.61,0.67,1.5,7.74,17.41,0,0.97,2,0,0,0,3,2,3,2,1,'no'],[38,9.0,5,5,98,490,0.07,13.68,35.81,6705.26,0.16,372.51,34,1,1,0,13,19,58,40,17,'no']]

att = [[5,2],[1,2],[0.9,2.2],[0.1,2.5],[0,0]]
classe = ['a','a','b','b','a']

lvq = lvq()

##lvq.config(att, classe, 2)
##c1, c2 = lvq.get_prototipos()
##
##print '\n',c1,'\n',c2

##lvq.config(att, classe, 2, 2)
##c1, c2 = lvq.get_prototipos()
##
##print '\n',c1,'\n',c2

lvq.config(att, classe, 2, 3)
c1, c2 = lvq.get_prototipos()

print '\n',c1,'\n',c2

##lvq1 = lvq1()
##lvq2 = lvq2()
##lvq3 = lvq3()
##
##print'LVQ1'
##lvq1.config(database2,4)
##conjunto1_att, conjunto1_classe =  lvq1.get_prototipos_att_classe()
##for i in range(len(conjunto1_att)):
##    print conjunto1_att[i],' - ', conjunto1_classe[i],'\n'
##
##print'LVQ2'
##lvq2.config(database2,4)
##conjunto2_att, conjunto2_classe =  lvq2.get_prototipos_att_classe()
##for i in range(len(conjunto2_att)):
##    print conjunto2_att[i],' - ', conjunto2_classe[i],'\n'
##    
##print'LVQ3'
##lvq3.config(database2,4)
##conjunto3_att, conjunto3_classe =  lvq3.get_prototipos_att_classe()
##for i in range(len(conjunto3_att)):
##    print conjunto3_att[i],' - ', conjunto3_classe[i],'\n'
    

