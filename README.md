# venver

Pythonの仮想環境（venv）を簡単に作成するためのツール

## 機能

- Pythonソースファイルから必要なパッケージを自動検出
- 仮想環境の作成と必要なパッケージのインストール
- パス情報をクリップボードにコピー

## 必要条件

- Python 3.x
- pyperclip

## インストール

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
# ソースファイルを指定して実行
python venver.py --sourceFiles path/to/your/script.py

# プロジェクト名を指定して実行
python venver.py --sourceFiles path/to/your/script.py --projectname myproject

# 特定のモジュールを指定して実行
python venver.py --modules numpy pandas matplotlib
```

## 出力

- 指定されたプロジェクト名で仮想環境を作成
- 必要なパッケージをインストール
- 仮想環境のPythonインタープリタのパスをクリップボードにコピー

## 注意事項

- `--system-site-packages`オプションを使用しているため、システムのパッケージも利用可能
- 一時ディレクトリ（temp）に仮想環境を作成 