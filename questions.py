# 题库 - 个人发展画像测试（36 道题 · 真实行为版）
# 每道题聚焦"你实际怎么做"，而非"你希望成为什么"

QUESTIONS = [
    # ── 第 1 题 ──
    {
        "id": 1,
        "question": "接到一个新任务时，你第一反应通常会做什么？",
        "options": [
            {"text": "先想这个任务有没有意思、值不值得做",
             "scores": {"creator": 1, "sensitive": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "先问做完有什么回报、对履历有没有帮助",
             "scores": {"driver": 1, "freedom": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}},
            {"text": "先看有没有标准流程可以照着做",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "先动手试试，边做边看情况",
             "scores": {"explorer": 1, "driver": 1, "creator": 0, "stable": 0, "sensitive": 0, "freedom": 0}}
        ]
    },
    # ── 第 2 题 ──
    {
        "id": 2,
        "question": "你做事情最常卡在哪个环节？",
        "options": [
            {"text": "开始之前想太多，迟迟迈不出第一步",
             "scores": {"creator": 1, "sensitive": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "做到一半觉得没意思，想做点别的",
             "scores": {"explorer": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "快做完时反复修改，总觉得还不够好",
             "scores": {"sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "做完就不管了，很少回头复盘",
             "scores": {"explorer": 1, "freedom": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0}}
        ]
    },
    # ── 第 3 题 ──
    {
        "id": 3,
        "question": "别人怎么说你你会最难受？",
        "options": [
            {"text": "说你做的东西没什么用",
             "scores": {"driver": 1, "freedom": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}},
            {"text": "说你的想法很幼稚",
             "scores": {"creator": 1, "sensitive": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "说你不靠谱、不让人放心",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "说你没什么特别、跟别人一样",
             "scores": {"freedom": 1, "sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0}}
        ]
    },
    # ── 第 4 题 ──
    {
        "id": 4,
        "question": "你学一样新东西时，实际最常出现的情况是？",
        "options": [
            {"text": "收藏了很多资料，但真正动手练的很少",
             "scores": {"creator": 1, "explorer": 1, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "跟着教程能做，一旦脱离教程就卡住",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "直接上手乱试，遇到问题再查怎么解决",
             "scores": {"explorer": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "只有当有一个具体作品目标时才会认真学",
             "scores": {"driver": 1, "explorer": 1, "creator": 0, "stable": 0, "sensitive": 0, "freedom": 0}}
        ]
    },
    # ── 第 5 题 ──
    {
        "id": 5,
        "question": "看到别人的好作品时，你更常出现哪种状态？",
        "options": [
            {"text": "下意识拆解它为什么好、怎么做到的",
             "scores": {"creator": 1, "explorer": 1, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "心里痒痒的，想自己也做一个类似的",
             "scores": {"explorer": 1, "driver": 1, "creator": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "有点受打击，觉得自己差太远",
             "scores": {"sensitive": 1, "creator": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "觉得挺好，但不太影响自己的状态",
             "scores": {"stable": 1, "freedom": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 6 题 ──
    {
        "id": 6,
        "question": "你做事最投入、效率最高的时候，通常是什么情形？",
        "options": [
            {"text": "刚开始接触一个新东西，觉得新鲜有趣",
             "scores": {"explorer": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "有明确的截止时间，必须出结果",
             "scores": {"driver": 1, "stable": 1, "creator": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "有人在等着看我的成果、期待我的表现",
             "scores": {"sensitive": 1, "driver": 1, "creator": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "有了清楚的步骤，每一步都知道该做什么",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}}
        ]
    },
    # ── 第 7 题 ──
    {
        "id": 7,
        "question": "事情搞砸了或者效果不好时，你第一反应通常是？",
        "options": [
            {"text": "找原因，看看哪里能改进",
             "scores": {"driver": 1, "stable": 1, "creator": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "怀疑自己是不是不适合做这个",
             "scores": {"sensitive": 1, "creator": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "想推翻重来、换个方向试试",
             "scores": {"explorer": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "先放着不管，过几天再说",
             "scores": {"freedom": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 8 题 ──
    {
        "id": 8,
        "question": "你最能接受的工作状态是哪种？",
        "options": [
            {"text": "事情重复，但标准清楚、不用动太多脑子",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "压力大，但结果和收入直接挂钩",
             "scores": {"driver": 1, "freedom": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}},
            {"text": "每天都有变化，能接触到新东西",
             "scores": {"explorer": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "没人管我，我自己安排节奏就行",
             "scores": {"freedom": 1, "creator": 1, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 9 题 ──
    {
        "id": 9,
        "question": "哪种工作环境会让你特别想走人？",
        "options": [
            {"text": "每天都做一模一样的事，感觉在浪费时间",
             "scores": {"explorer": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "领导说话难听、不尊重人",
             "scores": {"sensitive": 1, "freedom": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0}},
            {"text": "事情一团乱，没人说清楚到底该做什么",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "钱少、学不到东西、还被管得死死的",
             "scores": {"freedom": 1, "driver": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 10 题 ──
    {
        "id": 10,
        "question": "别人给你提意见时，你更能接受的是哪种方式？",
        "options": [
            {"text": "直接告诉我哪里错了、怎么改",
             "scores": {"driver": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "先肯定我的付出，再说改进方向",
             "scores": {"sensitive": 1, "explorer": 1, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}},
            {"text": "给我一个标准参考，我自己对比着改",
             "scores": {"stable": 1, "creator": 1, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "话好不好听无所谓，只要说得对就行",
             "scores": {"driver": 1, "freedom": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 11 题 ──
    {
        "id": 11,
        "question": "你想表达一个复杂想法时，通常会遇到什么问题？",
        "options": [
            {"text": "脑子里东西很多，但说的时候组织不起来",
             "scores": {"creator": 1, "explorer": 1, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "情绪一上来就说不清楚了",
             "scores": {"sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "能说清楚，但会讲得很长很绕",
             "scores": {"creator": 1, "stable": 1, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "不太喜欢说，更习惯直接做出来",
             "scores": {"driver": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}}
        ]
    },
    # ── 第 12 题 ──
    {
        "id": 12,
        "question": "你平时最多的内心想法通常会流向哪里？",
        "options": [
            {"text": "写成文字——设定、文案、随笔之类的",
             "scores": {"creator": 1, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "找人或 AI 聊出来",
             "scores": {"sensitive": 1, "explorer": 1, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}},
            {"text": "做成表格、清单、流程图",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "大部分放在心里，过一阵就忘了",
             "scores": {"creator": 1, "freedom": 1, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 13 题 ──
    {
        "id": 13,
        "question": "你对钱最真实的感受更接近哪一句？",
        "options": [
            {"text": "钱 = 自由，有钱才有选择权",
             "scores": {"freedom": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0}},
            {"text": "钱 = 安全感，有积蓄心里才踏实",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "钱 = 能力证明，赚多少钱体现多大本事",
             "scores": {"driver": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "钱 = 体验，能让我买喜欢的东西、去想去的地方",
             "scores": {"sensitive": 1, "freedom": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0}}
        ]
    },
    # ── 第 14 题 ──
    {
        "id": 14,
        "question": "你想象中理想的生活空间是什么样的？",
        "options": [
            {"text": "没人打扰，完全属于我自己的地方",
             "scores": {"freedom": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0}},
            {"text": "有人等我回来、有烟火气的地方",
             "scores": {"sensitive": 1, "explorer": 1, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}},
            {"text": "好看、整洁、有秩序感的空间",
             "scores": {"creator": 1, "stable": 1, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "能让我工作、创作、恢复能量的地方",
             "scores": {"driver": 1, "creator": 1, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}}
        ]
    },
    # ── 第 15 题 ──
    {
        "id": 15,
        "question": "你在人际关系中受伤后，通常的做法是？",
        "options": [
            {"text": "不主动说，等对方来发现自己不对",
             "scores": {"sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "用开玩笑或毒舌掩饰不舒服",
             "scores": {"freedom": 1, "sensitive": 0, "creator": 0, "driver": 0, "stable": 0, "explorer": 0}},
            {"text": "如果觉得对方不懂我，就慢慢冷下来",
             "scores": {"sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "提前降低期待，觉得这样就不会失望了",
             "scores": {"stable": 1, "freedom": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 16 题 ──
    {
        "id": 16,
        "question": "你跟人倾诉或求助时，最想要的是什么？",
        "options": [
            {"text": "希望对方能理解我的感受",
             "scores": {"sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "希望对方能帮我理清思路",
             "scores": {"creator": 1, "explorer": 1, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "希望对方直接告诉我该怎么办",
             "scores": {"stable": 1, "driver": 1, "creator": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "希望对方别废话，直接帮我一起把事情推完",
             "scores": {"driver": 1, "freedom": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 17 题 ──
    {
        "id": 17,
        "question": "你平时是怎么记录想法和灵感的？",
        "options": [
            {"text": "有想法当时就会记下来，比较有规律",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "偶尔记，但记得很乱，之后很少翻看",
             "scores": {"creator": 1, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "当时觉得肯定能记住，结果后来全忘了",
             "scores": {"creator": 1, "explorer": 1, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "只有特别强烈的灵感才会记，一般的不记",
             "scores": {"sensitive": 1, "explorer": 1, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}}
        ]
    },
    # ── 第 18 题 ──
    {
        "id": 18,
        "question": "回想你过去做过的项目或学习经历，你更接近哪种？",
        "options": [
            {"text": "准备很久才敢开始，资料要备齐才安心",
             "scores": {"stable": 1, "creator": 1, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "先搞一个粗糙版本出来，再慢慢改好",
             "scores": {"driver": 1, "explorer": 1, "creator": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "有人催或者有 deadline 才动得快",
             "scores": {"driver": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "兴趣来了猛干几天，兴趣没了就搁着",
             "scores": {"explorer": 1, "sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}}
        ]
    },
    # ── 第 19 题 ──
    {
        "id": 19,
        "question": "什么时候你会觉得自己挺有价值的？",
        "options": [
            {"text": "当别人没看懂的东西，我先看懂了",
             "scores": {"creator": 1, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "当我真的把一件事做完了、出了结果",
             "scores": {"driver": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "当我连续坚持做一件事很长时间",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "当我做出了别人看了有感觉的东西",
             "scores": {"sensitive": 1, "explorer": 1, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}}
        ]
    },
    # ── 第 20 题 ──
    {
        "id": 20,
        "question": "面对规则和流程，你真实的反应更接近哪种？",
        "options": [
            {"text": "讨厌被管，但自己又需要有规则才能自律",
             "scores": {"freedom": 1, "sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0}},
            {"text": "有清楚规则会让我心里踏实",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "规则能让事情更高效的话，我愿意遵守",
             "scores": {"driver": 1, "stable": 1, "creator": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "我更喜欢自己定规则，不想被别人安排",
             "scores": {"freedom": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 21 题 ──
    {
        "id": 21,
        "question": "你无聊或没事干的时候，最常做什么？",
        "options": [
            {"text": "刷手机看各种内容，找点刺激",
             "scores": {"sensitive": 1, "explorer": 1, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}},
            {"text": "开一个新坑——新想法、新项目、新兴趣",
             "scores": {"explorer": 1, "creator": 1, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "整理东西、做点顺手的小任务",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "琢磨一个现实目标，想办法推进它",
             "scores": {"driver": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}}
        ]
    },
    # ── 第 22 题 ──
    {
        "id": 22,
        "question": "你下决心做一件事之前，最纠结的一般是什么？",
        "options": [
            {"text": "做这件事到底有没有价值、能不能带来回报",
             "scores": {"driver": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "我到底是不是真的想做、有没有感觉",
             "scores": {"creator": 1, "sensitive": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "风险大不大、失败了怎么办",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "做了之后会不会被绑住、失去自由",
             "scores": {"freedom": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 23 题 ──
    {
        "id": 23,
        "question": "你更容易被什么样的内容或作品打动？",
        "options": [
            {"text": "人物关系复杂、越想越有后劲的那种",
             "scores": {"creator": 1, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "设定新鲜、有想象力的那种",
             "scores": {"explorer": 1, "creator": 1, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "结构完整严谨、细节经得起推敲的那种",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "情绪强烈、看了或听了会很上头的那种",
             "scores": {"sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}}
        ]
    },
    # ── 第 24 题 ──
    {
        "id": 24,
        "question": "如果完全不考虑现实限制，你最想成为的是哪种人？",
        "options": [
            {"text": "自由的人——有钱、有选择权、想去哪就去哪",
             "scores": {"freedom": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0}},
            {"text": "稳定的人——工作稳定、作息稳定、生活稳定",
             "scores": {"stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "有作品的人——能持续创作、被人记住",
             "scores": {"creator": 1, "sensitive": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "有结果的人——能解决问题、能赚钱、能推进事",
             "scores": {"driver": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}}
        ]
    },
    # ── 第 25 题 ──
    {
        "id": 25,
        "question": "你最常出现的自我怀疑是哪一种？",
        "options": [
            {"text": "我想的东西是不是其实很肤浅、不值一提",
             "scores": {"creator": 1, "sensitive": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "我是不是其实能力不行，之前的成绩都是运气",
             "scores": {"driver": 1, "sensitive": 1, "creator": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "我是不是永远没办法和别人一样稳定靠谱",
             "scores": {"stable": 1, "freedom": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0}},
            {"text": "我是不是选错了方向、浪费了时间",
             "scores": {"explorer": 1, "freedom": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0}}
        ]
    },
    # ── 第 26 题 ──
    {
        "id": 26,
        "question": "你一天中精力最好的那段时间，通常用来做什么？",
        "options": [
            {"text": "做需要深度思考和创作的事情",
             "scores": {"creator": 1, "explorer": 1, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "做最直接能产出结果、推进进度的事情",
             "scores": {"driver": 1, "stable": 1, "creator": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "处理那些需要耐心和细碎的重复事务",
             "scores": {"stable": 1, "sensitive": 1, "creator": 0, "driver": 0, "explorer": 0, "freedom": 0}},
            {"text": "刷手机、回消息、做一些不费脑子的事",
             "scores": {"explorer": 1, "sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}}
        ]
    },
    # ── 第 27 题 ──
    {
        "id": 27,
        "question": "与人发生冲突或意见严重不合时，你的本能反应是？",
        "options": [
            {"text": "沉默或者离开现场，不想当面冲突",
             "scores": {"sensitive": 1, "freedom": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0}},
            {"text": "马上反驳，用逻辑和证据证明自己是对的",
             "scores": {"driver": 1, "creator": 1, "stable": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "先顺着对方说，但心里会记着这笔账",
             "scores": {"stable": 1, "sensitive": 1, "creator": 0, "driver": 0, "explorer": 0, "freedom": 0}},
            {"text": "无所谓，你觉得对就去吧，我不想浪费精力",
             "scores": {"freedom": 1, "explorer": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0}}
        ]
    },
    # ── 第 28 题 ──
    {
        "id": 28,
        "question": "你答应别人的事情，实际完成情况更接近哪种？",
        "options": [
            {"text": "大部分都能高质量完成，答应了就会做到",
             "scores": {"stable": 1, "driver": 1, "creator": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "看心情，兴致好的时候做得很漂亮，没劲的时候就拖着",
             "scores": {"explorer": 1, "sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}},
            {"text": "当时答应是觉得应该答应，真要做的时候很痛苦",
             "scores": {"sensitive": 1, "freedom": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0}},
            {"text": "我很少答应人，答应了的都是经过考量的",
             "scores": {"creator": 1, "freedom": 1, "driver": 0, "stable": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 29 题 ──
    {
        "id": 29,
        "question": "面对大量信息涌入时，你通常怎么处理？",
        "options": [
            {"text": "先分类整理，建立框架，再逐个消化",
             "scores": {"creator": 1, "stable": 1, "driver": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "只看跟我当前目标相关的，其他的直接过滤",
             "scores": {"driver": 1, "freedom": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}},
            {"text": "每个都觉得有用，收藏起来以后再说",
             "scores": {"explorer": 1, "sensitive": 0, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}},
            {"text": "太多了就索性不看，断网清净一下",
             "scores": {"freedom": 1, "stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 30 题 ──
    {
        "id": 30,
        "question": "被人误解了而你解释不清时，你的真实反应是？",
        "options": [
            {"text": "反复解释，想让对方理解我真实的意思",
             "scores": {"creator": 1, "sensitive": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "算了，懂的人自然会懂，不想多说",
             "scores": {"freedom": 1, "explorer": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0}},
            {"text": "心里很难受，可能好几天都会想这件事",
             "scores": {"sensitive": 1, "creator": 0, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "无所谓，用结果证明自己，我做我的",
             "scores": {"driver": 1, "stable": 1, "creator": 0, "explorer": 0, "sensitive": 0, "freedom": 0}}
        ]
    },
    # ── 第 31 题 ──
    {
        "id": 31,
        "question": "你通常什么时候才会逼自己走出舒适区？",
        "options": [
            {"text": "当现在的事情让我感觉不到成长和意义的时候",
             "scores": {"explorer": 1, "creator": 1, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "当有一个明确的更高回报的目标摆在眼前时",
             "scores": {"driver": 1, "freedom": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}},
            {"text": "不太主动走出舒适区，除非被逼无奈",
             "scores": {"stable": 1, "sensitive": 0, "creator": 0, "driver": 0, "explorer": 0, "freedom": 0}},
            {"text": "一直都不太想待在舒适区里，定期就要折腾一下",
             "scores": {"explorer": 1, "freedom": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0}}
        ]
    },
    # ── 第 32 题 ──
    {
        "id": 32,
        "question": "看到同龄人或同行做得比你好很多时，你内心真实的状态是？",
        "options": [
            {"text": "分析他做对了什么，找自己的差距和机会",
             "scores": {"creator": 1, "explorer": 1, "driver": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "有点焦虑，马上想行动、不想被落下",
             "scores": {"driver": 1, "sensitive": 1, "creator": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "告诉自己每个人节奏不同，然后继续做自己的",
             "scores": {"stable": 1, "freedom": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0}},
            {"text": "不太会跟别人比，更在意自己有没有进步",
             "scores": {"freedom": 1, "stable": 1, "creator": 0, "driver": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 33 题 ──
    {
        "id": 33,
        "question": "你明明可以求助却选择自己硬扛的时候，最可能的原因是什么？",
        "options": [
            {"text": "觉得说出来对方也不一定懂我的问题",
             "scores": {"creator": 1, "sensitive": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "不想欠人情、不想显得自己能力不够",
             "scores": {"driver": 1, "freedom": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}},
            {"text": "习惯了什么都自己解决，不太会开口",
             "scores": {"stable": 1, "sensitive": 0, "creator": 0, "driver": 0, "explorer": 0, "freedom": 0}},
            {"text": "想试着自己搞定，搞不定再说",
             "scores": {"explorer": 1, "driver": 1, "creator": 0, "stable": 0, "sensitive": 0, "freedom": 0}}
        ]
    },
    # ── 第 34 题 ──
    {
        "id": 34,
        "question": "拒绝别人的请求时，你的真实感受更接近？",
        "options": [
            {"text": "内心会有负担，需要给自己做心理建设",
             "scores": {"sensitive": 1, "stable": 1, "creator": 0, "driver": 0, "explorer": 0, "freedom": 0}},
            {"text": "会衡量值不值得帮，不值得就直接拒绝",
             "scores": {"driver": 1, "freedom": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}},
            {"text": "不太会拒绝，经常答应了之后后悔",
             "scores": {"sensitive": 1, "explorer": 1, "creator": 0, "driver": 0, "stable": 0, "freedom": 0}},
            {"text": "拒绝得很干脆，不想浪费时间在不重要的事情上",
             "scores": {"freedom": 1, "driver": 1, "creator": 0, "stable": 0, "explorer": 0, "sensitive": 0}}
        ]
    },
    # ── 第 35 题 ──
    {
        "id": 35,
        "question": "你最近两年，自发坚持超过三个月的事情有几件？",
        "options": [
            {"text": "好几件——写作、学习、健身之类的，已经成了习惯",
             "scores": {"stable": 1, "driver": 1, "creator": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "一两件——但中间有中断，整体在持续",
             "scores": {"driver": 1, "explorer": 1, "creator": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "几乎没有超过三个月的，兴趣转移很快",
             "scores": {"explorer": 1, "freedom": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0}},
            {"text": "没有刻意坚持，但有一两件事一直没断过",
             "scores": {"creator": 1, "sensitive": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}}
        ]
    },
    # ── 第 36 题 ──
    {
        "id": 36,
        "question": "一件事做到 80% 和做到 100% 之间，你通常是怎样的状态？",
        "options": [
            {"text": "反复打磨细节，不做到满意不罢休",
             "scores": {"creator": 1, "sensitive": 1, "driver": 0, "stable": 0, "explorer": 0, "freedom": 0}},
            {"text": "快速收尾，先交付再说，后续再迭代",
             "scores": {"driver": 1, "explorer": 1, "creator": 0, "stable": 0, "sensitive": 0, "freedom": 0}},
            {"text": "按部就班做到结束，质量和速度都比较平均",
             "scores": {"stable": 1, "driver": 1, "creator": 0, "explorer": 0, "sensitive": 0, "freedom": 0}},
            {"text": "80% 之后就很难有动力收尾了，想搞新的",
             "scores": {"explorer": 1, "freedom": 1, "creator": 0, "driver": 0, "stable": 0, "sensitive": 0}}
        ]
    }
]
