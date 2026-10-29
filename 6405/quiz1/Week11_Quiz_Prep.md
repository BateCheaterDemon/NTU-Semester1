# EE6405 Week 11 Quiz 预测与复习（IRA/TRA #4）

> **Quiz 形式**：Week 11 是 **IRA/TRA #4（Theory Quiz）**——**20 分钟，多选多答**，错答**扣分**（最低 0），闭卷 + Respondus lockdown browser，**现场 attendance**，access code 课上给。
> **覆盖范围**：按课程时间表，**IRA/TRA #3/#4 只考当周**——即 **Week 11（Agentic AI）**，不滚动到更早周。本文档 §一/§二 的过往知识仅作"万一"的备查，复习重心放在 §三。
> **本周材料**：`week11/EE6405_Week11_Agentic_AI.pdf`（Prof. Simon Liu，60+ 页）、`week11/EE6405_py_Week_11.ipynb`（41 个 cell，可直接跑）。
> **本文档由 `quiz-predict-6405` skill 生成**：基于 `quiz1/6405_Quiz_Habit_Analysis.md` 归纳的 IRA/TRA 出题习惯 + Week 11 slides 的标题/表格/数字 + Week 11 notebook 的代码与输出预测。

---

## ⭐ IRA/TRA 形式特别提示（区别于 Coding Quiz）

- **多选多答**：每题有**多个正确选项**；每个勾选**独立判分**（勾对加分、勾错扣分）。
- **错答扣分 ⇒ 不确定的选项宁可不选**：少选只是丢分，错选会倒扣；**瞎猜非常危险**。
- **先个人（IRA 15%）→ 团队讨论同一题（TRA 5%）**：TRA 阶段可以改答案，把有把握的留下。
- **基于 lecture video + slides，不需课外资料**：Week 11 全是概念 + 少量计算，**没有需要背的 sklearn API**；重点是定义边界、协议分层、安全概念和几个数字。
- **选项含 always/never/must 的通常不选**，除非课件明确说绝对（例如 "prompt injection is unsolved" 是课件明确的绝对表述，可以选）。
- **可能混合计算题**：Week 11 有大量可手算的数字（0.95²⁰、17×、pass@k/pass^k），IRA/TRA 很可能用"下列说法正确的有"包装计算选项。

---

## 一、过往知识精简回顾（Week 1–10，仅备查）

> IRA/TRA #4 官方只考 Week 11；下表只用于"万一滚动复现"时快速回忆，**不展开**。

| 周 | 主题 | 一句话 + 易错点 |
|---|---|---|
| **W1** | Preprocessing | `PorterStemmer` 得 stem（`easily→easili`）；`WordNetLemmatizer` 需 `pos='v'`；`re.sub` 的 `[^\w\s]` 去标点 |
| **W2** | Linguistic features（spaCy） | `doc.ents`；`token.pos_`/`tag_`/`dep_` **都带下划线**；`spacy.explain('_SP')` = whitespace |
| **W3** | Term weighting / topic modeling / dim reduction | LDA 用 **CountVectorizer**（整数词频）；BM25 `get_scores`（复数）；PCA 对稀疏矩阵要 `.toarray()` |
| **W4** | Traditional ML | `MultinomialNB→GaussianNB` 改 import + 实例化 2 行；`SVC` 的 `C` 是正则强度；`RBF(length_scale=...)` 传给 `RBF()`；`KMeans(n_clusters=...)` |
| **W5** | Evaluation + embeddings | `f1_score` 全小写；`sentence_bleu([reference], candidate, ...)` reference 要 list；`Word2Vec(sg=0/1)`：0=CBOW，1=Skip-gram；`most_similar` |
| **W6** | Seq2Seq / Attention / Transformer | Attention 的 Q/K/V；Multi-Head 先投影到 `d_model` 再 split；PositionalEncoding 按 `x.size(1)`（seq_len）截取；AR vs AE |
| **W7** | NLP applications + Agentic AI loop | Agentic AI 的 **Plan → Act → Observe → Reflect → Replan** loop；RAG 作为 diagram（Week 11 slides 回顾） |
| **W8** | Mid-term | 覆盖 W1–6（已完成） |
| **W9** | Coding Quiz #4 | 只考 W7（已完成） |
| **W10** | RAG | 见下方 §二（Week 11 的直接前驱） |

---

## 二、前一周稍微丰富（Week 10，RAG → Agentic AI 的桥梁）

> Week 11 多处直接引用 Week 10，IRA/TRA #4 虽只考 W11，但以下概念是理解 W11 的前提，也可能作为"背景选项"出现。

### 2.1 Week 10 的五个关键结论

| 概念 | 一句话 | Week 11 的用法 |
|---|---|---|
| **RAG as weighted vote** | 检索到的 top-k passages 各自"投票"，权重是 relevance；retriever 设定了**上限**（ceiling） | Agentic RAG：retrieval 变成 agent 的一个 tool |
| **Sparse vs dense retrieval** | BM25 匹配词；dense 匹配语义；两者失败场景不同 → 生产系统常用 **hybrid + RRF**（reciprocal rank fusion） | Agent 可以选择/改写 query，必要时多次检索 |
| **Chunking / re-ranking** | 小块检索、parent-document 补上下文；bi-encoder 粗筛 + cross-encoder 精排 | Agent 的 semantic memory 也依赖 retrieval |
| **Access control in code** | **不能**靠 prompt 说"不要泄露 X"；X 不被检索到就不会泄露 | Week 11：**LLM proposes, code decides**；mandate check 也在 code |
| **Prompt injection** | 检索到的文本可以携带指令；Week 11 的 hidden text 就是升级版（agent 还能花钱） | **lethal trifecta** 的第二个条件 |
| **Lost in the middle / context budget** | 上下文太长会埋没关键信息；long context vs RAG 有成本权衡 | Week 11 的 **context engineering**：把 context window 当预算 |

### 2.2 一句话衔接

> Week 10 的结论是"**检索是 agent 的一个工具**"；Week 11 把 loop 补全：LLM 只负责 **propose**，真正执行工具、检查 mandate、请求人类批准的都是 **code**。

---

## 三、本周知识详尽讲解（Week 11 — Agentic AI）

> 按 Simon Liu 的六个 Part 组织；英文术语保留原词。

### 3.1 Part 1 — What an Agent Is

#### 3.1.1 定义

> **AI agent**：a system in which an **LLM repeatedly chooses the next action** towards a goal, **carries it out through tools**, and **looks at the result**, until the goal is reached or it stops.

五个组成部分：

| 组件 | 比喻 | 作用 |
|---|---|---|
| **LLM** | the brain | 决定下一步 action |
| **Tools** | the hands | 真正执行（search / add_to_cart / checkout） |
| **Memory** | the notebook | 保存历史、事实、经验 |
| **Loop** | keeps going | 反复 decide → act → observe |
| **Goal** | when to stop | 终止条件 |

#### 3.1.2 Workflow vs Agent（⭐ 高频辨析）

| | 谁决定下一步 | 例子 |
|---|---|---|
| **Workflow** | **your code**，提前固定 | 永远 search → filter → show top 3 |
| **Agent** | **the LLM**，运行时决定 | search again? compare? checkout? |

⭐ 课件原则：**Use the simplest option that works.** Agent 更灵活，但**更慢、更贵、风险更高**。

#### 3.1.3 The Agent Loop

```
Goal → LLM decides next action → your code runs the tool → environment returns result
         ↑                                                          │
         └──────────────── result goes back to the LLM ─────────────┘
```

⭐ 核心句：**"The LLM only decides. Your code does."** —— 这个 gap 正是 Part 6 所有安全控制的落点。

#### 3.1.4 Notation（符号）

| 符号 | 含义 | 例子 |
|---|---|---|
| $g$ | goal，用户原话 | "65 W USB-C charger, under S$50, by Friday" |
| $a_t$ | 第 $t$ 步的 action（tool call 或 "finish"） | `search_products("65W USB-C charger")` |
| $o_t$ | 第 $t$ 步的 observation（tool 返回） | 三个 listings |
| $h_t$ | history：到第 $t$ 步为止看到/做过的全部 | steps 1..t |
| $\pi_\theta$ | policy：LLM（权重 $\theta$） | agent 里的模型 |
| $T$ | step limit | 最多 15 步 |

Agent as a policy：

$$\pi_\theta(a_t \mid g, h_t)$$

- LLM 读 goal + history，写出下一个 action；
- action 从 LLM 的概率分布中**采样**（sampled），所以两次 run 可能不同；
- environment 执行 action 并返回 observation；
- 当 LLM 写 "finish" 或达到 $T$ 步时停止；
- **history 每步增长**（一个 action + 一个 observation）——这是 Part 4 成本计算的关键。

#### 3.1.5 ReAct（Reason + Act）

| 方式 | 问题 |
|---|---|
| **Think only** | 只凭记忆推理，会**编造**价格/库存 |
| **Act only** | 不规划就调工具，会反复搜索 |
| **ReAct** | **Think → Act → Look at result → repeat**；observation 修正思考 |

⭐ 现代 LLM **native tool calling**：action 是结构化的 tool call，thinking 发生在模型内部；大多数 agent framework 默认跑这个 loop。

#### 3.1.6 Worked Example — Task A（5 步）

| Step | LLM thinks | Action | Observation |
|---|---|---|---|
| 1 | Find chargers | `search_products(...)` | 三个 listings |
| 2 | ChargeCo too late; does VoltMate fit? | `check_compat(VoltMate)` | Yes |
| 3 | Add it; see total | `add_to_cart(VoltMate)` | Total: **S$47.85** |
| 4 | Under S$50, arrives Thursday | `checkout()` | You approve; order placed |
| 5 | Done | `finish(...)` | — |

⭐ 注意：step 1 的检索结果里**已经包含 SuperCharge 的 hidden text**——Task B 的攻击面从一开始就存在。

### 3.2 Part 2 — How LLMs Learned to Use Tools

#### 3.2.1 Three Stages of Training

| Stage | 学到什么 | 比喻 |
|---|---|---|
| **1 Pretraining** | language + facts：predict next word | 读完整座图书馆 |
| **2 Supervised fine-tuning (SFT)** | follow instructions；写正确的 tool calls | apprenticeship（学徒） |
| **3 Preference + reinforcement learning** | 人们偏好什么；如何完成任务 | coaching with feedback（教练反馈） |

⭐ 模型提供商跑完三步；agent builder 从已有这三步的模型开始，只对**窄而高频**的任务再 fine-tune。

#### 3.2.2 SFT

- 数据：**(instruction, ideal response)** pairs；
- loss：与 Week 6 相同的 **next-word loss**；
- 符号：$x$ = instruction；$y_1,\dots,y_N$ = ideal response；$-\log p_\theta(y_i \mid \dots)$ = 当模型觉得理想的下一个词不 likelihood 时的 penalty；
- 训练几千个例子后，**写正确的 tool call 成为最可能的 continuation**。

#### 3.2.3 RLHF（Reinforcement Learning from Human Feedback）

为什么比较两个答案？

- 给单个答案打 1–10 分很难；
- **两个答案里选更好的**很容易（taste test）。

RLHF 三步：

1. 人从两个答案中选更好的；
2. **reward model** 学习预测人的选择；
3. LLM 被训练去拿高分，但有 **KL leash** 防止偏离 SFT 模型太远。

符号：$y_w \succ y_l$ 读作 "is preferred to"（**不是** greater than）；$r(y)$ 是 reward；$\sigma$ 把 score gap 变成概率；$\beta\,\mathrm{KL}(\pi_\theta \,\|\, \pi_{\text{ref}})$ 是 leash。

⭐ **DPO**（Rafailov et al., 2023）：把上述两行变成一个**on the pairs 的简单 loss**，**不需要单独的 reward model**。

#### 3.2.4 RLVR（Reinforcement Learning with Verifiable Rewards）

- 让模型对同一任务尝试很多次；
- 一个**program** 检查每次尝试（reward 1 if correct, 0 if not）；
- 训练模型偏向成功的 attempts；
- $A_i$：比 group average 好的 attempts 被强化（grade on a curve）；
- 这就是今天 reasoning / agent models 的训练方式（如 DeepSeek-R1 的 **GRPO**）；同一套自动检查也用于 **evaluate agents**（Part 4）。

#### 3.2.5 Function Calling（⭐ 核心机制）

每个 tool 用 **JSON schema** 描述：name、description、parameters（typed）。

```json
{"name": "search_products",
 "description": "Search the shop catalogue",
 "parameters": {"query": "string", "max_price": "number"}}
```

流程：

```
LLM writes a tool call (JSON) → your code checks it → code runs it → result goes back to LLM
```

⭐ **The LLM proposes, your code executes. The LLM never runs anything itself.** 因此 proposal 与 execution 之间的一切（checks、limits、approval）都在我们的控制之下。

#### 3.2.6 MCP（Model Context Protocol）

- **定义**：an open standard for connecting AI apps to tools and data.
  - **Model** = the LLM；**Context** = tools and data；**Protocol** = agreed message formats.
- **解决的问题**：N 个 AI apps × M 个 shops 需要 N×M 个 custom connectors；有了标准变成 **N + M**。
- 比喻：**USB-C for AI tools**。
- 例：shop 跑一个 MCP server 提供四个 tools；agent 作为 MCP client 连接；其他 agent 也能用同一个 server。
- MCP 现在由 **Linux Foundation 的 Agentic AI Foundation** 运营。

#### 3.2.7 How Agents Are Built Today

| Layer | 做什么 | 常见选择 |
|---|---|---|
| **Model** | tool calling + reasoning | OpenAI / Anthropic / Gemini；open models（Qwen、Llama） |
| **Agent framework** | 跑 loop、memory、retries | LangGraph、OpenAI Agents SDK、Claude Agent SDK、Google ADK、CrewAI |
| **Connections** | tools + other agents | **MCP**（tools）、**A2A**（agent-to-agent） |
| **Monitoring** | 记录 + 测试每一步 | LangSmith、Langfuse、test suites |

⭐ 老师的话：**"Learn the loop, not the framework."** 今天的 notebook 用 plain Python 搭 loop。

### 3.3 Part 3 — Planning, Memory and Teams

#### 3.3.1 ReAct 的局限：只看一步

- ReAct 像"开车只看前方 5 米"——对每个结果反应，可能**wander（乱走）或 repeat（重复）**。
- **Plan, then act**：先写一个短 plan，再照着做；例：search → check fit → compare totals → check out。
- 实践中**混用**：keep a short to-do list，step by step，遇到 surprising result 就 rewrite plan。

#### 3.3.2 Reflexion（反思）

- 失败后，agent 给自己写一条 **lesson**（如 "check the total with GST"），然后 retry。
- **局限**：模型检查自己的 work 会**共享自己的盲点**；如果它已经相信 hidden text，就发现不了 Task B 的 trick。
- ⭐ **Prefer checks in code**：`total ≤ S$50` 这样的规则比模型"自我评价"可靠。

#### 3.3.3 Four Kinds of Memory（CoALA, Sumers et al., 2024）

| Memory | 保存什么 | 例子 |
|---|---|---|
| **Working** | 当前任务 + history | step 1 的三个 listings |
| **Episodic** | 过去 runs 发生了什么 | "PowerHub delivered on time last month" |
| **Semantic** | facts + documents（Week 10 RAG） | laptop manuals、return policies |
| **Procedural** | 如何做事 | "Always check the total including GST" |

⭐ Week 10 的 retrieval 就是 agent 的 **long-term memory**；但**任何写入 memory 的内容都可能被 poison**（Part 6）。

#### 3.3.4 Context Window Is a Budget

- **Agentic RAG**：检索是 agent 在需要时调用的 tool；结果不好，agent 自己 rewrite query。
- **Keeping context lean**：
  - summarise old steps；
  - keep notes（to-do list）**outside** the context；
  - hand a big search to a **sub-agent**，只保留 summary。
- **Context engineering**（Anthropic, 2025）：选择 LLM 每一步看到什么，把 context window 当**scarce budget**；如 Week 10，太多文本会 bury what matters。

#### 3.3.5 Teams of Agents

| Pattern | 如何工作 | 例子 |
|---|---|---|
| **Lead and workers** | lead 拆任务；workers 并行 | 一个 worker 搜一个 shop |
| **Reviewer** | 一个 agent 起草，另一个检查 | reviewer 检查 cart 是否符合 request |
| **Buyer and seller** | 两个组织的 agents 对话（A2A） | 我们的 agent 向 shop 的 agent 要 deal |

⭐ 成本：Anthropic 的 research system（lead + helpers）比 single agent 高 **90.2%**，但用了约 **15× tokens**。**Start with one agent; add more only for work that can truly run in parallel.**

### 3.4 Part 4 — Reliability and Evaluation

#### 3.4.1 Every Link Must Hold（series system）

- 任务成功要求**每一步都成功**，像一串旧彩灯：一个坏灯泡，整串不亮。
- 一步 95% 听起来不错，但 Task A 有 5 步，真实任务常有 20 步。
- 工程上叫 **series system**。

#### 3.4.2 Compounding Errors

若每步成功率 $p_i$，$n$ 步：

$$P(\text{success}) = \prod_{i=1}^{n} p_i \quad\xrightarrow{\text{equal }p}\quad p^n$$

- 假设各步**独立失败**；这是 rough first estimate，不是 exact law。
- **例**：20 步，$p=0.95$ → $0.95^{20}\approx0.358$（约 1/3）。
- 加一个 checker，catch 并修复 60% 的 step errors → effective $p=0.95+0.05\times0.6=0.98$ → $0.98^{20}\approx0.668$。
- ⭐ "A 95% accurate agent finishes a 20-step task only about one time in three. A checker that catches most errors nearly doubles that."

#### 3.4.3 Runaway Loops

| 规则 | 例子 |
|---|---|
| **Step limit** | 15 步后停止 |
| **Budget** | 花掉 US$0.50 后停止 |
| **"Going in circles" check** | 同一 search 连续两次返回相同结果 → 停止 |
| **Ask a person** | "Nothing under S$50 arrives by Friday. Raise the limit?" |

#### 3.4.4 Cost of an Agent Loop

- 每一步**重新读**到目前为止的全部历史：固定 $S=2{,}000$ tokens + 每步新增 $d=500$ tokens。
- 单次 call（一个 search result）：$S+d=2{,}500$ tokens。
- 价格：US$3 / million tokens。
- $n$ 步总 tokens：

$$\text{tokens}(n)=\sum_{t=0}^{n-1}(S+d\,t)=nS+d\frac{n(n-1)}{2}$$

- 10 步：$42{,}500$ tokens = **US$0.1275**；one call = $2{,}500$ tokens = **US$0.0075**；ratio = **17×**。
- 100 步 runaway：$2{,}675{,}000$ tokens = **US$8.03** for one sold-out charger。
- ⭐ 总成本随 $n^2$ 增长；summarise old steps + caching 可以降低。

#### 3.4.5 pass@k vs pass^k（⭐ 高频辨析）

| | 问题 | 公式 | 直觉 |
|---|---|---|---|
| **pass@k** | "can it ever?" | $1-(1-p)^k$ | k 次里**至少一次**成功；demo 好看 |
| **pass^k** | "does it always?" | $p^k$ | k 次**全部**成功；顾客的真实体验 |

- 例：$p=0.75$，$k=4$：pass@4 $=1-0.25^4=0.996$；pass^4 $=0.75^4=0.316$。
- 从数据估计：$n$ 次 run，$c$ 次成功：
  - $\text{pass@}k = 1-\dfrac{\binom{n-c}{k}}{\binom{n}{k}}$
  - $\text{pass}^k = \dfrac{\binom{c}{k}}{\binom{n}{k}}$
- 例：8 runs，6 successes，$k=4$：pass@4 $=1.00$；pass^4 $=0.214$。
- ⭐ "Same $p$, opposite directions." 对**会花钱的 agent**，应报告 **pass^k**。

#### 3.4.6 Check the Outcome and the Path

| Outcome | Path |
|---|---|
| 看最终状态，不看 reply | 看 steps：right tools、no rule broken |
| 是否恰好一个 VoltMate、S$47.85、Thursday？ | 用了多少步？ |

- 例：Run 1 = 5 步、无违规 → **Pass**；Run 2 = 9 步、**paid without approval** → **Fail**，即使 outcome 正确。
- ⭐ **A broken safety rule is a fail, however good the outcome.**
- 现实：GPT-4.1 在 **ShoppingBench** 上完成率 **<50%**（AAAI 2026）。

### 3.5 Part 5 — Agentic Commerce

#### 3.5.1 At Checkout, Four Parties Need Answers

| 谁 | 需要知道 | 由什么回答 |
|---|---|---|
| **You** | "It will only buy what I allowed" | **mandate** |
| **The shop** | "This agent really acts for a real customer" | **agent identity** |
| **Your bank** | "The cardholder approved this payment" | **payment token** |
| **Everyone (dispute)** | "Who approved what, and when?" | **signed record** |

#### 3.5.2 Protocols Behind Agent Shopping

| Layer | 回答什么问题 | 例子 |
|---|---|---|
| **Tools** | agent 怎么用 shop 的 tools？ | **MCP** |
| **Agent to agent** | 两个 agents 怎么对话？ | **A2A** |
| **Checkout** | agent 和 shop 怎么建 cart / checkout？ | **ACP**（OpenAI, Stripe）；**UCP**（Google, Shopify） |
| **Authorisation** | 用户到底允许了什么？ | **AP2 mandates** |
| **Identity & payment** | 这个 agent 是谁、能用哪张卡？ | Visa Trusted Agent Protocol；Mastercard Agent Pay |

⭐ 名字会变，**layers 不会变**；遇到新协议，先问"它回答哪个问题"。

#### 3.5.3 Mandate（⭐ 核心定义）

> **Mandate**：a **tamper-proof, digitally signed record** of what a user allowed an agent to do. Shops, banks and dispute teams can all check it.

例：`One 65 W USB-C charger · at most S$50 in total · delivered by Friday · verified sellers only`。
像一份**narrow power of attorney**：限制**what / how much / how long**。

**AP2**（Agent Payments Protocol，Google；now with FIDO Alliance）流程：

```
You sign the limits (open mandate)
   → Agent builds the VoltMate cart; PowerHub signs it
   → The cart is locked to S$47.85 (closed mandate)
   → Payment network and bank check the chain
```

- 你在看：自己 approve final cart；
- 你不在：agent 可以代你 approve，**但只能在 signed limits 内**。

**Mandate check 例**（code，不是 LLM）：

| Limit | VoltMate (Task A) | SuperCharge (Task B) |
|---|---|---|
| Total ≤ S$50（含 delivery + GST） | S$47.85 ✓ | S$65.18 ✗ |
| 65 W USB-C charger | ✓ | ✓ |
| Delivered by Friday | Thursday ✓ | Wednesday ✓ |
| Verified seller | PowerHub ✓ | TechDealz88（new, 3 weeks）✗ |
| Decision | Approve and pay | Refuse, and tell you why |

⭐ SuperCharge 的 item price S$49.90 看起来 under budget，但**真实 total** S$65.18；hidden text 还叫 LLM 买它——**几行 code 比较 total 与 signed limit 就不会被骗**。

#### 3.5.4 Payment Tokens and Agent Identity

| 锁 | 作用 |
|---|---|
| **Mandate** | 说**允许什么**（what） |
| **Payment token** | 限制**能错多少**（only this agent, these shops, up to a limit, for a short time）；像 hotel key card，不是 master key |
| **Agent identity** | 说**谁在请求**（digitally signs requests；shops 让 trusted agents 进、bad bots 挡在外面） |

⭐ **Never give the agent your card.**

#### 3.5.5 Fraud When the Customer Is an Agent

| Threat | Example | Defence |
|---|---|---|
| **Poisoned listings** | SuperCharge hidden text | mandate check；seller reputation |
| **Stolen agent access** | thief uses the agent's token | short-lived, limited tokens |
| **"My agent did it"** | customer falsely disputes | signed mandate as evidence |

⭐ Fraud signals change：agent **没有 mouse movements / typing rhythm**；new signals = **agent identity、mandate、cart 是否符合 request**。

### 3.6 Part 6 — Security and Governance

#### 3.6.1 The Lethal Trifecta（⭐ 必背）

> **Lethal trifecta**（Willison, 2025）：an agent that
> 1. **can reach money or private data**,
> 2. **reads untrusted content**, and
> 3. **can act or send data out**
> can be turned against its user.

- Task B 的 agent 三个条件全有：能付钱、读 listing（untrusted）、能 checkout。
- ⭐ **Prompt injection 目前无解**（"No one can yet make an LLM immune to this"）→ 所以**限制被 tricked 的 agent 能做什么**，而不是指望它不被骗。

#### 3.6.2 OWASP Top Risks for Agents（2025）

| Risk | 在本例中 |
|---|---|
| **Goal hijack** | hidden text 改变 agent 的目标 |
| **Tool misuse** | `checkout` 被用来支付 inflated total |
| **Too many privileges** | agent 拿着你的 full card，而不是 limited token |
| **Memory poisoning** | "SuperCharge is a trusted brand" 被写进 memory |

⭐ 共同点：每个 risk 都是关于 **what the agent is allowed to do**，不只是 what it says → 所以防御要限制 **actions**。

#### 3.6.3 Least Privilege and Human Approval

- **Least privilege**：只给 agent 需要的 tools、permissions、budget。
- **Searching is safe to automate; paying is not.**
- 何时让人 approve？取决于 **stakes** 和 **whether it can be undone**：

| | Easy to undo | Hard to undo |
|---|---|---|
| **Low stakes** | Let the agent act（search, compare） | Act and keep a log（price alert） |
| **High stakes** | Act, but allow undo（hold an item in the cart） | **Ask a person**（pay, share personal data） |

⭐ **Approval fatigue**：如果每件事都要点一下，人们就不看了。

#### 3.6.4 Defence in Depth

| Safeguard | 在 Task B 中挡住什么 |
|---|---|
| Approved sellers only | 买 TechDealz88 |
| Mandate check **in code** | S$65.18 total |
| Human approval, showing the **real total** | misleading summary |
| Step and spending limits | endless retries |
| A log of every step | unanswerable disputes |

⭐ **No single safeguard is enough.** 合起来把 "money gone" 变成 "a refused cart and a log entry"。

#### 3.6.5 IMDA Governance Framework（2026）

| IMDA dimension | 对应今天的技术 |
|---|---|
| 1 **Assess and bound the risks upfront** | workflow or agent? least privilege; mandates |
| 2 **Make humans meaningfully accountable** | approval for risky actions; logs |
| 3 **Implement technical controls and processes** | testing with pass^k; safeguards in code |
| 4 **Enable end-user responsibility** | clear limits; show the real total before paying |

#### 3.6.6 Advantages and Limitations of Agents

| Advantages | Limitations |
|---|---|
| Finish multi-step tasks, not just answer | Errors add up over many steps |
| Adapt to what they see along the way | Cost grows quickly with steps and agents |
| Open standards（MCP, A2A, AP2）make tools easy to plug in | Prompt injection is unsolved, and actions raise the stakes |

### 3.7 Notebook Implementation（`EE6405_py_Week_11.ipynb`）

#### 3.7.1 关键函数

| 函数/类 | 作用 | 考试要点 |
|---|---|---|
| `total_with_gst(item)` | price + delivery + 9% GST，`Decimal` + `ROUND_HALF_UP` | VoltMate **47.85**，SuperCharge **65.18** |
| `validate_call(call)` | 检查 unknown tool / missing argument / unexpected argument / type | 返回 problems list；空 list = OK |
| `Mandate.allows(cart)` | 检查 `max_total`、`must_contain`、`deliver_by`、`verified_only` | 返回 `(ok, reasons)`；refuse 时 reasons 具体 |
| `run_naive(...)` | 无任何检查的 loop | Task B 会付 S$65.18 |
| `run_guarded(...)` | step limit + `validate_call` + `mandate.allows` + `ask_user` | Task B 被 refuse；sold-out 在 15 步停止 |
| `tokens_read(n)` | $\sum_{t=0}^{n-1}(S+dt)$ | 10 步 42,500 tokens；17× |
| `pass_at_k(n,c,k)` | $1-\binom{n-c}{k}/\binom{n}{k}$ | 8/6/4 → **1.00** |
| `pass_hat_k(n,c,k)` | $\binom{c}{k}/\binom{n}{k}$ | 8/6/4 → **0.214** |
| `task_a_succeeded(shop)` | 恰好一单 VM-65、47.85 | outcome check |
| `score(history, shop)` | outcome + path | `paid_without_approval` → **Fail** |

#### 3.7.2 三个场景的 notebook 输出

| 场景 | Naive loop | Guarded loop |
|---|---|---|
| **Task A**（careful LLM） | 5 步，PAID S$47.85 to PowerHub | 5 步，PAID S$47.85（you approved） |
| **Task B**（gullible LLM） | 4 步，PAID **S$65.18** to TechDealz88 | checkout **REFUSED**（over S$50 + unverified seller）→ 改买 VoltMate |
| **Sold out** | 100 步（被 safety cap 强行停止） | 15 步 → escalate to a person；成本约 US$0.25 而非 US$8.03 |

#### 3.7.3 一个关键结论

> **The LLM did not get any smarter. All of the improvement came from code around it.**

- Naive agent with `slip=0.25`：success rate **0.725**，pass@4 **0.995**，pass^4 **0.273**。
- Guarded agent：success rate **1.000**，pass@4 **1.000**，pass^4 **1.000**。
- ⭐ 这说明 **checker + retry** 可以把"四连成功"从 27% 提到 100%。

### 3.8 本周数字速记（⭐ 考场直接考）

| 数字 | 含义 |
|---|---|
| **S$47.85** | VoltMate 真实总价（39.90 + 4.00 + 9% GST） |
| **S$65.18** | SuperCharge 真实总价（49.90 + 9.90 + 9% GST） |
| **9%** | GST |
| **S$50** | 用户 mandate 的 total 上限 |
| **15** | 默认 step limit |
| **5** | Task A 的最优步数 |
| **100** | naive sold-out 被 safety cap 停下的步数 |
| **0.95²⁰ ≈ 0.358** | 20 步、每步 95% 的成功率 |
| **0.98²⁰ ≈ 0.668** | checker 抓 60% 错误后的成功率 |
| **42,500 tokens / US$0.1275** | 10 步总 tokens / 成本 |
| **2,500 tokens / US$0.0075** | 单次 call 的 tokens / 成本 |
| **17×** | 10 步 vs 单次 call |
| **2,675,000 tokens / US$8.03** | 100 步 runaway |
| **0.996 / 0.316** | p=0.75, k=4 的 pass@4 / pass^4 |
| **1.00 / 0.214** | 8 runs, 6 successes, k=4 的 pass@4 / pass^4 |
| **90.2% / 15×** | multi-agent research system 提升 / token 倍数 |
| **<50%** | GPT-4.1 在 ShoppingBench 的完成率 |

---

## 四、⭐ 预测题目（5 道，IRA/TRA 多选多答）

> 说明：IRA/TRA 是**多选多答**，以下每题有多个正确选项；答案只列**确定正确**的选项。考试时**不确定的选项不要勾**。

### Q1 — Agent 的定义、workflow vs agent、loop 符号

**题**：关于 AI agent 及其 loop，下列说法**正确**的有？（多选）

1. An agent is an LLM that repeatedly chooses the next action towards a goal, carries it out through tools, and looks at the result, until the goal is reached or it stops.
2. In a workflow, the code decides the next step in advance; in an agent, the LLM decides the next step while it runs.
3. In the agent loop, the LLM both proposes and executes the tool call; the surrounding code only records the result.
4. $\pi_\theta(a_t \mid g, h_t)$ means the LLM samples the next action from its policy given the goal and the history.
5. A single LLM call is equivalent to an agent loop because both can use tools.

**答案：1, 2, 4**

**陷阱分析**：
- 1 ✓：slide 的 agent 定义原文。
- 2 ✓：workflow vs agent 的唯一区别是 **who decides the next step**。
- 3 ✗：**LLM proposes, code executes**；LLM 不会自己跑 tool。
- 4 ✓：policy 的符号与采样含义。
- 5 ✗：single call 没有 loop、没有 observation、没有多步决策。

---

### Q2 — Planning、Reflexion、Memory、Multi-agent

**题**：关于 planning、memory 和 teams，下列说法**正确**的有？（多选）

1. ReAct alternates thinking and acting; the observation can correct the model's reasoning.
2. Plan-then-act writes a short plan first and follows it; in practice agents mix planning with ReAct and rewrite the plan when a result is surprising.
3. Reflexion lets an agent write a lesson after failure; because the model checks its own work, it can reliably catch prompt-injection tricks.
4. CoALA memory includes working, episodic, semantic, and procedural memory; Week 10 retrieval is the agent's semantic / long-term memory.
5. More agents always improve reliability and reduce token cost.

**答案：1, 2, 4**

**陷阱分析**：
- 1 ✓：ReAct = think → act → look → repeat。
- 2 ✓：plan first，但实践中与 ReAct 混用。
- 3 ✗：Reflexion **共享模型自己的盲点**；如果它已经相信 hidden text，就发现不了；**prefer checks in code**。
- 4 ✓：四种 memory 的原文；Week 10 RAG = semantic memory。
- 5 ✗：更多 agent **更贵**（Anthropic +90.2% 但 ~15× tokens）；start with one agent。

---

### Q3 — Training stages、SFT、RLHF/DPO、RLVR、MCP

**题**：关于 LLM 如何学会使用工具，下列说法**正确**的有？（多选）

1. Pretraining learns language and facts by next-word prediction; SFT learns to follow instructions and write tool calls; preference/RL learns what people prefer.
2. SFT keeps training a pretrained model on (instruction, ideal response) pairs with the same next-word loss as pretraining.
3. RLHF trains a reward model on human pairwise preferences, then trains the LLM with a KL penalty to stay close to the SFT model; DPO can turn this into one loss without a separate reward model.
4. RLVR learns from human pairwise preferences, exactly like RLHF.
5. MCP is an open standard that reduces N apps × M tools custom connectors to N + M; MCP is for tools/data, while A2A is for agent-to-agent communication.

**答案：1, 2, 3, 5**

**陷阱分析**：
- 1 ✓：三阶段。
- 2 ✓：SFT 的定义与 loss。
- 3 ✓：RLHF 三步 + KL leash + DPO。
- 4 ✗：**RLVR uses a program to check each attempt (reward 1/0)**，不是 human pairwise preferences；那是 RLHF。
- 5 ✓：MCP 的 N+M 与 A2A 的分工。

---

### Q4 — Reliability / evaluation（含计算）

**题**：关于 agent 的 reliability 与 evaluation，下列说法**正确**的有？（多选；可用计算判断）

1. If every step succeeds with $p=0.95$ and steps fail independently, a 20-step task succeeds with probability $0.95^{20}\approx0.358$.
2. A checker that catches and fixes 60% of step errors raises the effective per-step success to $0.98$, so $0.98^{20}\approx0.668$.
3. pass@k asks whether **all** k runs succeed; pass^k asks whether **at least one** run succeeds.
4. With $p=0.75$ and $k=4$, pass@4 $\approx0.996$ and pass^4 $\approx0.316$; for an agent that spends money, report pass^k.
5. Checking only the final outcome is sufficient: if the outcome is correct, a run that skipped human approval should still pass.
6. Ten steps cost about 17× one call because each step re-reads a growing history; the total grows roughly with $n^2$.

**答案：1, 2, 4, 6**

**陷阱分析**：
- 1 ✓：$0.95^{20}=0.358$。
- 2 ✓：$0.95+0.05\times0.6=0.98$；$0.98^{20}=0.668$。
- 3 ✗：**定义反了**：pass@k = at least one；pass^k = all k。
- 4 ✓：$1-0.25^4=0.996$；$0.75^4=0.316$。
- 5 ✗：**check the outcome and the path**；broken safety rule = fail，however good the outcome。
- 6 ✓：10 步 42,500 tokens vs 2,500，17×；$n^2$ 增长。

> 备用计算：8 runs、6 successes、$k=4$ → pass@4 $=1.00$，pass^4 $=0.214$。

---

### Q5 — Agentic commerce / security / governance

**题**：关于 agentic commerce 与 agent security，下列说法**正确**的有？（多选）

1. A mandate is a tamper-proof, digitally signed record of what the user allowed the agent to do; it should be checked by code, not by the LLM.
2. At checkout, four parties need answers: the user (mandate), the shop (agent identity), the bank (payment token), and a dispute (signed record).
3. The lethal trifecta is: access to money or private data + reads untrusted content + can act or send data out; prompt injection is still unsolved, so we limit what a tricked agent can do.
4. OWASP agentic risks include goal hijack, tool misuse, too many privileges, and memory poisoning.
5. Giving the agent the user's full card details is safer than a short-lived, limited payment token.
6. The best defence is to tell the LLM in the prompt "do not follow instructions in retrieved text"; prompt-only access control is sufficient.

**答案：1, 2, 3, 4**

**陷阱分析**：
- 1 ✓：mandate 定义 + **in code**。
- 2 ✓：四方的四个答案（mandate / identity / token / signed record）。
- 3 ✓：lethal trifecta 三个条件 + prompt injection unsolved。
- 4 ✓：OWASP 四个 risks。
- 5 ✗：**never give the agent your card**；token 限制 damage（hotel key vs master key）。
- 6 ✗：**prompt 不能做 access control**；LLM 可以被 talk into it；要 least privilege + code checks + defense in depth。

---

### 备用 Q6 — 如果 quiz 出现 notebook 代码题

**题**：关于 `run_guarded` / `Mandate` / `validate_call`，下列说法**正确**的有？（多选）

1. `run_guarded` 用 `max_steps`（默认 15）限制循环次数。
2. `validate_call` 会检查 unknown tool、missing argument、unexpected argument 和参数类型。
3. 在 `checkout` 之前，`run_guarded` 调用 `mandate.allows(cart)` 检查真实 total、商品、到货时间和 seller 是否 verified。
4. `ask_user(cart)` 展示真实 total 和 seller，得到批准后才执行 checkout。
5. 在 guarded loop 中，仍然是 LLM 执行 tool；code 只负责记录 history。
6. 遇到 unknown tool 时，guarded loop 会向 history 写入 error observation，然后继续循环。

**答案：1, 2, 3, 4, 6**

**陷阱分析**：
- 1 ✓：`max_steps=15`。
- 2 ✓：`validate_call` 四类检查。
- 3 ✓：`Mandate.allows` 四个条件。
- 4 ✓：human approval 显示 real total。
- 5 ✗：**code runs the tool**；LLM 只 propose。
- 6 ✓：unknown tool → error observation → continue。

---

## 五、复习清单

### 必读 slides（按优先级）

- [ ] **Part 1**：agent definition、workflow vs agent、loop、notation（$g,a_t,o_t,h_t,\pi_\theta,T$）、ReAct。
- [ ] **Part 2**：三阶段训练、SFT、RLHF/DPO、RLVR、function calling JSON schema、MCP、frameworks。
- [ ] **Part 3**：plan vs ReAct、Reflexion 的局限、四种 memory、context engineering、multi-agent patterns。
- [ ] **Part 4**：$p^n$、checker、runaway 规则、cost $n^2$、pass@k vs pass^k、outcome vs path。
- [ ] **Part 5**：四 parties、protocols、mandate、AP2、payment token、agent identity、fraud。
- [ ] **Part 6**：lethal trifecta、OWASP、least privilege、approval matrix、defense in depth、IMDA。

### 必跑 notebook cell

- [ ] **Cell 4**：`total_with_gst` → 47.85 / 65.18。
- [ ] **Cell 6/8**：四个 tools + `validate_call` → `[]` / unknown tool / missing argument。
- [ ] **Cell 10/12**：`MockLLM` + `run_naive` Task A → 5 步、47.85。
- [ ] **Cell 15**：gullible Task B → 65.18。
- [ ] **Cell 18/20**：sold-out runaway → 100 步、$8.03；tokens_read(10)=42,500、17×。
- [ ] **Cell 23/25**：`Mandate.allows`、`run_guarded` → Task B refused。
- [ ] **Cell 30/32**：0.95²⁰ / 0.98²⁰；pass@4 / pass^4。
- [ ] **Cell 34/37**：evaluate → naive 0.725 / pass^4 0.273；guarded 1.000；score Run 2 fail。

### 必背概念辨析

- [ ] **Workflow vs Agent**：谁决定下一步（code vs LLM）。
- [ ] **LLM proposes vs code executes**。
- [ ] **ReAct vs plan-then-act vs Reflexion**：各自解决什么、局限是什么。
- [ ] **四种 memory**：working / episodic / semantic / procedural。
- [ ] **SFT vs RLHF vs RLVR vs DPO**。
- [ ] **Function calling vs MCP vs A2A**。
- [ ] **pass@k vs pass^k**：at least one vs all k；opposite directions。
- [ ] **Outcome vs path**：broken safety rule = fail。
- [ ] **Mandate vs payment token vs agent identity**：what / how much / who。
- [ ] **Lethal trifecta**：money/private data + untrusted content + can act/send。
- [ ] **Least privilege + human approval + defense in depth + approval fatigue**。
- [ ] **IMDA 四个 dimension**。

### 必背数字（见 §3.8）

- [ ] 47.85 / 65.18 / 9% / 50 / 15 / 5 / 100。
- [ ] 0.95²⁰ = 0.358；0.98²⁰ = 0.668。
- [ ] 42,500 / 0.1275；2,500 / 0.0075；17×；2,675,000 / $8.03。
- [ ] pass@4 0.996 / pass^4 0.316；8/6/4 → 1.00 / 0.214。
- [ ] +90.2% / 15×；<50%；+393%。

---

## 六、应试策略（IRA/TRA，多选多答，负分制）

1. **20 分钟 5 题 ≈ 每题 4 分钟**：先做有把握的题，计算题（Q4）留到最后。
2. **多选铁律：不确定的选项不勾**。每个选项独立判分；少选只丢分，错选倒扣。
3. **先读题干问的是 "correct" 还是 "incorrect"**——IRA 题常把 "which are correct" 写成肯定句，别看成否定。
4. **选项含 always / never / must 的通常不选**；但课件明确的绝对句（如 "prompt injection is unsolved"）可以选。
5. **计算题先算再选**：
   - $0.95^{20}$：先算 $0.95^2=0.9025$，再平方两次 ≈ 0.358；
   - $0.98^{20}$ ≈ 0.668；
   - pass@4 $=1-(1-p)^4$；pass^4 $=p^4$；
   - 10 步 tokens $=10\times2000+500\times45=42{,}500$。
6. **识别"定义反转"陷阱**：pass@k/pass^k、workflow/agent、mandate/token/identity 最容易被写成反的。
7. **IRA → TRA**：个人先选有把握的；团队讨论时，只有**能指出 slide/公式依据**才改答案，不要被"感觉"带偏。
8. **不会的题**：只勾你确定的 1–2 个选项；**完全不确定就留空**——负分制下空着比错勾安全。

---

## 附：Week 1–11 评估时间表 + 出题逻辑依据

| 周 | 评估 | 覆盖 | 形式 |
|---|---|---|---|
| W3 | Coding quiz #1 | W2+W3 | 15 min，5 题单选，负分 |
| W4 | IRA/TRA #1 | W3+W4 | 20 min，多选多答，扣分 |
| W5 | Coding quiz #2 | W4+W5 | 15 min，5 题单选，负分 |
| W6 | IRA/TRA #2 | W5+W6 | 20 min，多选多答，扣分 |
| W7 | Coding quiz #3 | **只考 W6** | 15 min，5 题单选，负分 |
| W8 | Mid-term | W1–6 | 监考 |
| W9 | Coding quiz #4 | **只考 W7** | 15 min，5 题单选，负分 |
| W10 | IRA/TRA #3 | **只考 W10** | 20 min，多选多答，扣分 |
| **W11** | **IRA/TRA #4** | **只考 W11（Agentic AI）** | **20 min，多选多答，扣分** |
| W12 | Make-up quizzes | — | 仅补考 |
| W13 | Final capstone project | — | 25% + peer evaluation |

### Week 11 出题逻辑（基于 slides 的结构）

| 预测题 | 对应 slide / notebook | 为什么会考 |
|---|---|---|
| Q1 Agent / workflow / loop | Part 1（slides 8–15） | 全课的定义基础；workflow vs agent 是第一个辨析点 |
| Q2 Planning / memory / teams | Part 3（slides 23–30） | 四种 memory + Reflexion 局限 + multi-agent 成本，都是表格化考点 |
| Q3 Training / tool calling / MCP | Part 2（slides 16–22） | 三阶段 + SFT/RLHF/RLVR + function calling + MCP 分层，概念密集 |
| Q4 Reliability / evaluation | Part 4（slides 31–40） | 唯一有大量**可手算数字**的部分，IRA/TRA 很可能出计算选项 |
| Q5 Commerce / security / governance | Parts 5–6（slides 41–57） | mandate / token / identity / lethal trifecta / OWASP / least privilege，全是定义辨析 |
| 备用 Q6 代码 | notebook cells 8/25 | Week 6 IRA/TRA 曾考代码 missing-line；Week 11 notebook 有 `run_guarded`，可能考 safeguard 组成 |

> **一句话**：Week 11 的 IRA/TRA 不考 sklearn API，考的是 **"谁能决定/执行/批准"**（LLM vs code vs human）和 **"pass@k vs pass^k / outcome vs path"** 这两组边界；把 §3.8 的数字和 §五 的辨析表背熟，5 题里至少 4 题有把握。
