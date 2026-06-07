# 행소박물관 유물 4지선다 퀴즈
# 마우스로 보기를 선택하면 정답 또는 오답을 확인할 수 있습니다.

import sys

import pygame


pygame.init()

# 화면 설정
WIDTH, HEIGHT = 1100, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("행소박물관 유물 4지선다 퀴즈")
clock = pygame.time.Clock()

# 색상 설정
BG = (244, 238, 224)
PANEL = (255, 252, 244)
INK = (48, 44, 38)
MUTED = (111, 103, 90)
ACCENT = (109, 47, 40)
ACCENT_LIGHT = (228, 208, 187)
BUTTON = (238, 226, 205)
BUTTON_HOVER = (225, 207, 178)
CORRECT = (82, 145, 95)
WRONG = (190, 78, 67)
WHITE = (255, 255, 255)

# 글꼴 설정
title_font = pygame.font.SysFont("malgungothic", 42, bold=True)
question_font = pygame.font.SysFont("malgungothic", 27, bold=True)
button_font = pygame.font.SysFont("malgungothic", 23, bold=True)
small_font = pygame.font.SysFont("malgungothic", 18)
small_bold_font = pygame.font.SysFont("malgungothic", 18, bold=True)

# 퀴즈 문제
questions = [
    {
        "question": "돌을 깨뜨려 날카로운 날을 만든 구석기시대 유물은 무엇일까요?",
        "choices": ["뗀석기", "청동거울", "백자", "기와"],
        "answer": 0,
    },
    {
        "question": "표면에 빗살 모양의 무늬가 있는 대표적인 신석기시대 유물은?",
        "choices": ["민무늬토기", "빗살무늬토기", "청자", "철제 갑옷"],
        "answer": 1,
    },
    {
        "question": "청동기시대를 대표하는 칼 모양의 유물은 무엇일까요?",
        "choices": ["돌도끼", "철제 낫", "비파형동검", "청화백자"],
        "answer": 2,
    },
    {
        "question": "청동기시대 유물인 반달돌칼은 주로 어디에 사용했을까요?",
        "choices": ["곡식의 이삭을 따는 일", "글씨를 쓰는 일", "옷을 만드는 일", "물을 담는 일"],
        "answer": 0,
    },
    {
        "question": "가야 고분에서 출토된 철제 갑옷과 투구로 알 수 있는 것은?",
        "choices": ["종이 제작 기술", "철기 제작과 무장 문화", "유리 공예 기술", "인쇄 기술"],
        "answer": 1,
    },
    {
        "question": "가야 토기인 굽다리접시의 생김새로 알맞은 것은 무엇일까요?",
        "choices": ["바닥이 완전히 평평하다", "손잡이가 두 개 달렸다", "뚜껑만 있고 그릇은 없다", "그릇 아래에 높은 굽이 달렸다"],
        "answer": 3,
    },
    {
        "question": "사람이나 동물의 모습을 흙으로 빚어 만든 작은 유물은 무엇일까요?",
        "choices": ["석탑", "금관", "토우", "청동검"],
        "answer": 2,
    },
    {
        "question": "고려청자의 대표적인 색깔은 무엇일까요?",
        "choices": ["비취색", "붉은색", "검은색", "노란색"],
        "answer": 0,
    },
    {
        "question": "상감청자의 무늬는 어떤 방법으로 만들었을까요?",
        "choices": ["종이를 붙였다", "무늬 홈에 다른 색 흙을 채웠다", "나무 조각을 붙였다", "금속으로 겉을 감쌌다"],
        "answer": 1,
    },
    {
        "question": "분청사기의 특징으로 알맞은 것은 무엇일까요?",
        "choices": ["금으로만 만들었다", "유리로 만들었다", "흰 흙으로 자유롭게 장식했다", "나무를 깎아 만들었다"],
        "answer": 2,
    },
    {
        "question": "조선시대 백자의 대표적인 특징은 무엇일까요?",
        "choices": ["화려한 금빛", "맑고 깨끗한 흰색", "투명한 유리 재질", "거친 돌 표면"],
        "answer": 1,
    },
    {
        "question": "청화백자의 푸른 무늬를 그릴 때 사용한 안료는 무엇일까요?",
        "choices": ["먹", "황토", "숯", "코발트 안료"],
        "answer": 3,
    },
    {
        "question": "울산 천전리 각석에서 볼 수 있는 것으로 알맞은 것은 무엇일까요?",
        "choices": ["도자기 무늬", "왕의 금관", "바위에 새긴 그림과 글자", "목조 불상"],
        "answer": 2,
    },
    {
        "question": "행소박물관 소장 보물인 진주성도는 어떤 유물일까요?",
        "choices": ["진주성 모습을 그린 지도", "왕이 입던 갑옷", "불교 경전", "청동으로 만든 종"],
        "answer": 0,
    },
    {
        "question": "행소박물관 소장 구운몽도는 무엇을 그림으로 표현한 유물일까요?",
        "choices": ["농사 방법", "전쟁 지도", "소설 구운몽의 장면", "별자리 관측 기록"],
        "answer": 2,
    },
]

# 게임 상태
current_question = 0
score = 0
message = ""
message_color = INK
selected_answer = -1
answer_time = 0
quiz_finished = False

# 보기 버튼 위치
button_rects = [
    pygame.Rect(90, 285, 440, 92),
    pygame.Rect(570, 285, 440, 92),
    pygame.Rect(90, 397, 440, 92),
    pygame.Rect(570, 397, 440, 92),
]


def draw_text(text, font, color, x, y, center=False):
    image = font.render(text, True, color)
    rect = image.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(image, rect)


def draw_background():
    screen.fill(BG)
    pygame.draw.rect(screen, ACCENT, (0, 0, WIDTH, 18))
    pygame.draw.circle(screen, ACCENT_LIGHT, (75, 655), 130, 3)
    pygame.draw.circle(screen, ACCENT_LIGHT, (1025, 72), 105, 3)


def draw_quiz():
    draw_background()
    question = questions[current_question]

    # 진행 상황
    draw_text(f"문제 {current_question + 1} / {len(questions)}", small_bold_font, ACCENT, 90, 45)
    draw_text(f"점수 {score}", small_bold_font, ACCENT, 950, 45)
    progress_width = int(920 * (current_question + 1) / len(questions))
    pygame.draw.rect(screen, ACCENT_LIGHT, (90, 78, 920, 12), border_radius=6)
    pygame.draw.rect(screen, ACCENT, (90, 78, progress_width, 12), border_radius=6)

    # 문제 출력
    question_box = pygame.Rect(90, 115, 920, 125)
    pygame.draw.rect(screen, PANEL, question_box, border_radius=22)
    pygame.draw.rect(screen, ACCENT_LIGHT, question_box, 2, border_radius=22)
    draw_text(question["question"], question_font, INK, WIDTH // 2, 178, center=True)

    # 보기 버튼 출력
    mouse_pos = pygame.mouse.get_pos()
    for i, rect in enumerate(button_rects):
        color = BUTTON_HOVER if rect.collidepoint(mouse_pos) else BUTTON
        text_color = INK

        if selected_answer != -1:
            if i == question["answer"]:
                color = CORRECT
                text_color = WHITE
            elif i == selected_answer:
                color = WRONG
                text_color = WHITE

        pygame.draw.rect(screen, color, rect, border_radius=18)
        pygame.draw.rect(screen, ACCENT, rect, 2, border_radius=18)
        pygame.draw.circle(screen, ACCENT, (rect.x + 42, rect.centery), 20)
        draw_text(str(i + 1), small_bold_font, WHITE, rect.x + 42, rect.centery, center=True)
        draw_text(question["choices"][i], button_font, text_color, rect.centerx + 20, rect.centery, center=True)

    # 정답 / 오답 텍스트
    if message:
        draw_text(message, button_font, message_color, 90, 535)
        draw_text("잠시 후 다음 문제로 이동합니다.", small_font, MUTED, 90, 575)
    else:
        draw_text("마우스로 정답을 선택해 주세요.", small_font, MUTED, WIDTH // 2, 555, center=True)


def draw_result():
    draw_background()
    draw_text("QUIZ COMPLETE", small_bold_font, ACCENT, WIDTH // 2, 120, center=True)
    draw_text("퀴즈 종료!", title_font, INK, WIDTH // 2, 190, center=True)

    pygame.draw.circle(screen, PANEL, (WIDTH // 2, 340), 112)
    pygame.draw.circle(screen, ACCENT, (WIDTH // 2, 340), 112, 8)
    draw_text(str(score), title_font, ACCENT, WIDTH // 2, 320, center=True)
    draw_text(f"/ {len(questions)}", button_font, MUTED, WIDTH // 2, 375, center=True)

    if score >= 12:
        result_message = "훌륭합니다! 행소박물관 유물을 잘 이해했어요."
    elif score >= 8:
        result_message = "좋아요! 조금만 더 공부하면 더 잘할 수 있어요."
    else:
        result_message = "아쉬워요. 행소박물관 유물을 다시 학습해보세요."

    draw_text(result_message, button_font, INK, WIDTH // 2, 500, center=True)
    draw_text("ESC 키를 누르면 종료됩니다.", small_font, MUTED, WIDTH // 2, 650, center=True)


# 메인 반복문
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not quiz_finished and selected_answer == -1:
            for i, rect in enumerate(button_rects):
                if rect.collidepoint(event.pos):
                    selected_answer = i
                    answer_time = pygame.time.get_ticks()

                    if i == questions[current_question]["answer"]:
                        score += 1
                        message = "정답입니다!"
                        message_color = CORRECT
                    else:
                        message = "아쉬워요. 정답을 확인해 보세요."
                        message_color = WRONG

    if not quiz_finished and selected_answer != -1:
        if pygame.time.get_ticks() - answer_time >= 1000:
            current_question += 1
            selected_answer = -1
            message = ""

            if current_question >= len(questions):
                quiz_finished = True

    if quiz_finished:
        draw_result()
    else:
        draw_quiz()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
