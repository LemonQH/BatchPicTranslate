import  os
from pictranslate import connect

class Translate():
    def __init__(self,name,file_paths,result_root_path,trans_type):
        self.name=name
        self.file_paths=file_paths
        self.result_root_path=result_root_path
        self.trans_type=trans_type


    def translate_files(self):
        for file_path in self.file_paths:
            file_name=os.path.basename(file_path)
            print('==========='+file_path+'===========')
            trans_reult=self.translate_use_netease(file_path)
            print(trans_reult)
            resul_file=open(self.result_root_path+'/result_'+file_name.split('.')[0]+'.txt','w').write(trans_reult)


    def translate_use_netease(self,file_content):
        result= connect(file_content)
        return result