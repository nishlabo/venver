import subprocess
import tempfile
import os
import pyperclip
import Utils
import ast

class Venver():
	import_to_pip_map = {
		'PIL': 'Pillow',
		'sklearn': 'scikit-learn',
		'cp2': 'opencv-python',  # cp2のインポートに対応するpipパッケージ名
		# 他にも必要なマッピングを追加
	}
	def __init__(self, sourceFiles, modules=None, projectname=None):
		sf=sourceFiles
		if not modules:
			self.modules=self.missings(self.extract_libraries_from_code(sf))
		else:
			self.modules=modules
		if not projectname:
			self.projectname=os.path.splitext(os.path.split(sf)[1])[0]
		else:
			self.projectname=projectname

	def extract_libraries_from_code(self, code):
		'''ファイルから読み込んだコードをast木にして、import文/from文をリストアップします'''
		tree = ast.parse(Utils._read(code))
		libraries = set()  # 重複を防ぐためセットを使用
		for node in ast.walk(tree):
			if isinstance(node, ast.Import):
				for alias in node.names:
					libraries.add(alias.name)
			elif isinstance(node, ast.ImportFrom):
				libraries.add(node.module)
		return list(libraries)


	def missings(self, libs):
		'''import文を仮にimportして、できないものをリストアップします。import/installで名称の異なるものはリストに従って変更します'''
		missinglibs=[]
		for l in libs:
			try:
				__import__(l)
			except ImportError:
				if l in self.import_to_pip_map:
					missinglibs.append(self.import_to_pip_map[l])
				else:
					missinglibs.append(l)	
		# TODO: requirements.txt をソースファイルと同じ場所に作成しておく
		return missinglibs


	def venv_prepare(self, proj, mods):
		commands=[
["python", "-m", "venv", wk:=os.path.join(tempfile.gettempdir(), proj), "--system-site-packages"],
[py:=os.path.join(wk,"Scripts","python.exe"), "-m", "pip", "install", "--upgrade", "pip"]]+[
[py, "-m", "pip", "install", "--upgrade", m] for m in mods]

		for command in commands:
			subprocess.run(command)
		return py

if __name__=="__main__":
	wk,args=Utils.premain2({'sourceFiles':None,"modules":None,"projectname":"venv"},['sourceFiles'])

	v=Venver(args.sourceFiles[0])
	py=v.venv_prepare(v.projectname, v.modules)
	print(py)
	pyperclip.copy(py)
