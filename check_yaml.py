import yaml
import sys

try:
    with open('c:/Users/ys907/Documents/workspace/projects/pj_game_archive/_config.yml', 'r', encoding='utf-8') as f:
        yaml.safe_load(f)
    print("YAML is valid")
except yaml.YAMLError as exc:
    print(f"YAML error: {exc}")
except Exception as e:
    print(f"Error: {e}")
