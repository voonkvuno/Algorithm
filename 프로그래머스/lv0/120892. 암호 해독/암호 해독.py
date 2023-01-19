def solution(cipher, code):
    return ''.join(v for i, v in enumerate(cipher, start=1) if not i%code)