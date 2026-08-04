import json
from copy         import deepcopy
from pathlib      import Path
from default_quiz import DEFAULT_QUIZZES

STATEFile = Path(__file__).with_name("state.json")

def default_state():
    return {
        "quizzes":      deepcopy(DEFAULT_QUIZZES),
        "best_score":   0,
        "best_correct": 0,
        "best_total":   0,
        "history":      [],
    }

def loadstate():
    try:
        with STATEFile.open("r", encoding="utf-8") as f:
            state = json.load(f)
        if not isinstance(state, dict) or not isinstance(state.get("quizzes"), list):
            raise ValueError
        return state
    
    except FileNotFoundError:    print("파일을 찾을 수 없습니다. 기본 퀴즈를 불러옵니다.")
    except json.JSONDecodeError: print("파일이 올바른 JSON 형식이 아닙니다. 기본 퀴즈를 불러옵니다.")
    except ValueError:           print("데이터가 올바르지 않습니다. 기본 퀴즈를 불러옵니다.")
    except OSError:              print("파일을 읽을 수 없습니다. 기본 퀴즈를 불러옵니다.")
    return default_state()

def savestate(state):
    try:
        with STATEFile.open("w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=4)
        return True
    except (OSError, TypeError):
        print("파일을 저장할 수 없습니다.")