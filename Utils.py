import argparse
import os

def _read(filename):
    """ファイルを読み込んで文字列として返す"""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def premain2(defaults, required):
    """コマンドライン引数を処理する
    
    Args:
        defaults (dict): デフォルト値の辞書
        required (list): 必須パラメータのリスト
    
    Returns:
        tuple: (作業ディレクトリ, 引数のNamespace)
    """
    parser = argparse.ArgumentParser()
    for k, v in defaults.items():
        if k in required:
            parser.add_argument(f"--{k}", required=True, nargs=None if isinstance(v, str) else '*')
        else:
            parser.add_argument(f"--{k}", default=v, nargs=None if isinstance(v, str) else '*')
    
    args = parser.parse_args()
    
    # 作業ディレクトリを取得
    wk = os.getcwd()
    
    return wk, args 