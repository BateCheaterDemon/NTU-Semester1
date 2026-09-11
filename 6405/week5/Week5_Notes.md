# EE6405 Week 5 知识点 — Neural Language Models + Hyperparameter Tuning

> 课程：EE6405 Natural Language Processing（Dr. S. Supraja）
> 来源：`week5/` 文件夹下材料
> - `EE6405_W4_NM_For Students.pdf`（Neural Language Models 课件，Dr. Simon Liu）— RNN/LSTM/GRU/BiRNN
> - `EE6405_W5_HPT_For Students.pdf`（HyperParameter Tuning 课件，Dr. S. Supraja）— K-Fold CV / Optimizers / Loss / Batch / LR / Epochs / Early Stopping / Gradient Clipping
> - `Week 6.ipynb`（Neural Language Models notebook：RNNModel/LSTMModel/GRUModel/BiRNNModel + 训练循环）
> - `Week 8(1).ipynb`（HyperParameter Tuning notebook：GridSearchCV + KFold + LSTMClassifier + gradient clipping）
> - `Week6MCQ.md`（5 题，RNN/LSTM/BiRNN/optimizer/lr 代码题）
> - `Week8MCQ.md`（5 题，GridSearchCV/KFold/LSTMClassifier/clip_grad_value_ 代码题）
> - `Week 5 tasks.pdf`（team discussion：vanilla RNN vs LSTM vs GRU + 3 个超参探索）
>
> **说明**：本周无录播转写，基于课件/notebook/MCQ/tasks 整理。保留英文术语原词，中文用于释义连接。
> ⚠️ 文件命名注意：`week5/` 文件夹里的 notebook 叫 `Week 6.ipynb` 和 `Week 8(1).ipynb`，但对应的是 Week 5 的两堂课（Neural Language Models + HyperParameter Tuning）；`Week 5.ipynb`（Evaluation Metrics + Word Embeddings）反而在 `week4/` 文件夹里，属 Week 4 课堂延续。

---

## 一、本周主线

Week 4 讲完传统 ML（Naïve Bayes / SVM / ELM / Gaussian Process / 聚类）后，本周转入**深度学习序列模型**——回答"**如何让神经网络处理有顺序的文本数据**"。主线：

1. **Sequential data（序列数据）**为什么需要特殊模型 → 传统前馈网络的三大局限。
2. **RNN**：用 hidden state 记忆历史 → 但有 vanishing/exploding gradient。
3. **LSTM**：用三道 gate（forget/input/output）+ cell state 解 vanishing gradient。
4. **GRU**：LSTM 简化版，两道 gate（reset/update），更省算力。
5. **Bi-RNN**：双向，同时看过去和未来。
6. **Hyperparameter Tuning**：如何调优上述神经网络（K-Fold CV、optimizer、loss、batch size、learning rate、epochs、early stopping、gradient clipping）。

> ⭐ **本周有 Coding Quiz #2**（15 分钟，5 题单选，负分制，闭卷 + Respondus lockdown browser），考 Week 4 + Week 5 内容。Week5MCQ（在 `week4/` 文件夹）是 Evaluation Metrics + Word Embeddings 的题；Week6MCQ（在 `week5/` 文件夹）是 RNN/LSTM/BiRNN 的题——两者都是本周考点信号。

---

## 二、Sequential Data（序列数据）

### 2.1 什么是 Sequential Data

- **Sequential data**：按特定顺序组织的数据，常带时间或时序关系。数据点出现的**顺序对理解意义至关重要**。
- **文本是典型的 sequential data**：句子的意义取决于词的顺序与语法规则；一个词的含义会因上下文（前后文）而改变。

### 2.2 传统模型的三大局限

传统模型（如 simple linear regression、basic feedforward neural network）处理序列数据有三大问题：

| 局限 | 含义 |
|---|---|
| **Lack of Memory（无记忆）** | 无法记住或捕捉序列内的 long-term dependency |
| **Order Insensitivity（对顺序不敏感）** | 把数据当无序处理，不理解顺序的重要性 |
| **Variable-Length Limitation（变长限制）** | 只能处理固定长度输入，但序列常是变长的 |

→ 需要能捕捉 temporal dependency 的模型：**RNN、LSTM、GRU、Bi-directional Network、Transformer（下周）**。

---

## 三、Recurrent Neural Networks（RNN，循环神经网络）

### 3.1 核心思想

- RNN 是为**序列/时间序列数据**设计的神经网络。
- 与 feedforward NN 不同，RNN 有**自循环连接**（loop back on themselves），能**记忆之前的输入**。
- 可建模**时间上的 dependency**，适合 language translation、speech recognition、time series prediction。

### 3.2 公式

- 每个 RNN unit 用前一个状态和当前输入算新的 hidden state：
  $$h_t = g(x_t, h_{t-1})$$
- （可选地）用当前 hidden state 算输出：
  $$y_t = f(h_t)$$
- **Hidden state** $h_t \in \mathbb{R}^D$ 是连续向量，可表示很丰富的信息，甚至整个历史。

### 3.3 Vanilla RNN（最简形式）

- Generic RNN：$h_t = g(x_t, h_{t-1})$，$y_t = f(h_t)$。
- **Vanilla RNN**（最简单形式）：
  $$h_t = \tanh(Ux_t + Wh_{t-1} + b)$$
  $$y_t = \mathrm{softmax}(Vh_t)$$

### 3.4 参数共享（Parameter Sharing / Tied Parameters）

- RNN 的参数在**所有时间步共享**（unlike feedforward NN）——同一组 $U, W, V$ 用于每个时间步。
- 这是它能处理**变长序列**的关键。

### 3.5 三种架构

| 架构 | 输入→输出 | 用例 |
|---|---|---|
| **Sequence-to-One** | 一个序列 → 一个标签 | Sentiment Analysis（情感分析） |
| **One-to-Sequence** | 一个输入 → 一个序列 | Image Captioning（图像描述） |
| **Sequence-to-Sequence** | 一个序列 → 一个序列 | POS tagging、Named Entity Recognition |

- Sequence-to-One：$h_t = g(x_t, h_{t-1})$，$y = f(h_n)$（只用最后一步 hidden state）。
- Sequence-to-Sequence：每一步都输出 $y_t = f(h_t)$。

### 3.6 Activation Functions

| 函数 | 公式 | 用途 | 优缺点 |
|---|---|---|---|
| **Sigmoid** | $\sigma(x) = \frac{1}{1+e^{-x}}$ | gate、分类输出层 | 优：非线性、平滑；缺：非零中心、vanishing gradient |
| **Tanh** | $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ | RNN/LSTM 的 hidden state & cell | 优：零中心、比 sigmoid 收敛快；缺：仍会 vanishing gradient |

- 关系：$\tanh(x) = 2\sigma(2x) - 1$。

### 3.7 RNN 的局限 — Vanishing / Exploding Gradient

- **Vanishing Gradient**：长序列上梯度变得太小，难以学习远距离信息。
- **Exploding Gradient**：梯度变得太大，训练不稳定。
- **Memory Limitation**：短期记忆有限，因 vanishing gradient 难记序列早期信息。
- 课件图示：$\frac{\partial s_t}{\partial s_{t-1}}$ 连乘导致梯度指数衰减/爆炸。

→ **LSTM** 就是为解决 vanishing gradient 而设计。

### 3.8 notebook 代码（`Week 6.ipynb` cell 3）

```python
class RNNModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_size):
        super(RNNModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_size)

    def forward(self, x):
        x = self.embedding(x)
        out, _ = self.rnn(x)
        out = self.fc(out)
        return out
```

- `nn.Embedding(vocab_size, embedding_dim)`：把词索引转成 dense vector（见 §六 6.2 MCQ Q1）。
- `nn.RNN(embedding_dim, hidden_dim, batch_first=True)`：`batch_first=True` 表示输入 shape 是 `(batch, seq, feature)`。
- `self.fc = nn.Linear(hidden_dim, output_size)`：最后线性层映射到输出。
- `out, _ = self.rnn(x)`：RNN 返回 `(output, h_n)`，`h_n` 是最后 hidden state（这里用 `_` 丢弃）。

> ⭐ **Week6MCQ Q1**：`self.embedding` 层的作用？**答案：To convert input sequences of indices into dense vector representations.**（把索引序列转成 dense vector）。干扰项：linear transformation of RNN output（那是 `fc`）、initialize hidden states、activation function、concatenate layers。

---

## 四、Long Short-Term Memory（LSTM，长短期记忆网络）

### 4.1 核心思想

- LSTM 是 RNN 的一种变体，**专为解决 vanishing gradient problem 而设计**。
- 引入**gating mechanism**：forget gate、input gate、output gate，选择性添加/保留/删除信息，防止梯度在长序列中消失。
- **Cell state（细胞状态）**代表 long-term memory，由三道 gate 调控。

### 4.2 Cell State（细胞状态）

- Cell state 代表**长期记忆**。
- 由三道 gate（forget/input/output）选择性 add / retain / remove 信息。
- 使 LSTM 能捕捉和保留 **long-term dependency**。

### 4.3 三道 Gate

#### Forget Gate（遗忘门）
- 决定 cell state 中**保留多少长期信息**。
- 前一 hidden state 与当前输入过 sigmoid：
  $$f_t = \sigma(W_f \cdot h_{t-1} + x_t + b_f)$$
- 输出接近 0 = forget，接近 1 = keep。

#### Input Gate（输入门）
- 决定**加入什么新信息**到 cell state。
- sigmoid 决定更新哪些值 + tanh 生成候选内容：
  $$i_t = \sigma(U_i x_t + W_i h_{t-1} + b_i)$$
  $$\tilde{c}_t = \tanh(U_c x_t + W_c h_{t-1} + b_c)$$

#### Cell State Update（细胞状态更新）
- 由 forget gate 和 input gate 结果组合更新：
  $$c_t = f_t c_{t-1} + i_t \tilde{c}_t$$

#### Output Gate（输出门）
- 决定 cell state 的哪部分用于生成当前输出。
  $$o_t = \sigma(U_o x_t + W_o h_{t-1} + b_{(o)})$$
- hidden state：
  $$h_t = o_t \tanh(c_t)$$

### 4.4 notebook 代码（`Week 6.ipynb` cell 5）

```python
class LSTMModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_size):
        super(LSTMModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_size)

    def forward(self, x):
        x = self.embedding(x)
        out, _ = self.lstm(x)
        out = self.fc(out)
        return out
```

- `nn.LSTM(embedding_dim, hidden_dim, batch_first=True)`：与 `nn.RNN` 接口一致，换类名即可。
- LSTM 返回 `(output, (h_n, c_n))`——同时有 hidden state 和 cell state。

> ⭐ **Week6MCQ Q3**：从 RNNModel 改成 LSTM 需改什么？**答案：`self.rnn = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)`**（只换 `nn.RNN` → `nn.LSTM`，其余不变）。干扰项：加 `padding_idx=0`（embedding 参数，不需要）、改 `fc` 为 `hidden_dim*2`（那是 bidirectional）。

---

## 五、Gated Recurrent Unit（GRU，门控循环单元）

### 5.1 核心思想

- GRU（2014）是 LSTM 的**简化变体**，用更少的 gate 和参数达到类似效果。
- **无单独 cell state**，把 cell state 和 hidden state 的角色合并。
- 因此**计算成本更低**。

### 5.2 两道 Gate

| Gate | 作用 | 公式 |
|---|---|---|
| **Reset Gate（重置门）** | 控制前一 hidden state 被遗忘多少 | $r_t = \sigma(W_r \cdot h_{t-1} + x_t + b_r)$ |
| **Update Gate（更新门）** | 控制前一 hidden state 保留多少 + 新候选加多少 | $z_t = \sigma(W_z \cdot h_{t-1} + x_t + b_z)$ |

- Reset gate 缩放前一 hidden state，与当前输入组合过 tanh 生成候选 hidden state $\tilde{h}_t$。
- Update gate 在前一 hidden state 和新候选之间做加权组合，得最终 hidden state。

### 5.3 notebook 代码（`Week 6.ipynb` cell 7）

```python
class GRUModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_size):
        super(GRUModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.gru = nn.GRU(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_size)

    def forward(self, x):
        x = self.embedding(x)
        out, _ = self.gru(x)
        out = self.fc(out)
        return out
```

- `nn.GRU` 与 `nn.RNN`/`nn.LSTM` 接口完全一致，只换类名。

### 5.4 RNN vs LSTM vs GRU 选择（Week 5 tasks Q1）

- **Vanilla RNN**：短序列、计算资源有限、不需要长记忆时用。
- **LSTM**：长序列、需捕捉 long-term dependency、可接受较高计算成本时用。
- **GRU**：想要 LSTM 的效果但计算资源更紧、或序列中等长度时用——参数更少、训练更快，效果常接近 LSTM。
- 三者选择无定论，取决于任务与数据，靠实验（hyperparameter tuning，见 §七）决定。

---

## 六、Bi-Directional RNNs（Bi-RNN，双向 RNN）

### 6.1 核心思想

- Bi-RNN 由**两个独立 RNN**组成：一个**正向**（forward）走输入序列，一个**反向**（backward）走。
- 特别适合**需要同时理解过去和未来上下文**的任务（如 NER、POS tagging——一个词的标签常由其前后词决定）。
- LSTM 和 GRU 常用于 Bi-RNN。

### 6.2 notebook 代码（`Week 6.ipynb` cell 9）

```python
class BiRNNModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_size):
        super(BiRNNModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_dim * 2, output_size)   # 注意 *2

    def forward(self, x):
        x = self.embedding(x)
        out, _ = self.rnn(x)
        out = self.fc(out)
        return out
```

- 关键两处改动（相对 RNNModel）：
  1. `nn.RNN(..., bidirectional=True)`——开启双向。
  2. `self.fc = nn.Linear(hidden_dim * 2, output_size)`——正向和反向各输出 `hidden_dim`，**拼接后是 `hidden_dim * 2`**。

> ⭐ **Week6MCQ Q2**：从 RNNModel 改成 bidirectional RNN 需改什么？
> **答案**：
> ```python
> self.rnn = nn.RNN(embedding_dim, hidden_dim, batch_first=True, bidirectional=True)
> self.fc = nn.Linear(hidden_dim * 2, output_size)
> ```
> 必须**同时**改 `bidirectional=True` 和 `fc` 输入维度 `hidden_dim * 2`。干扰项：只改一个、`bidirectional=True` 但不 `*2`、漏 `embedding_dim`/`hidden_dim` 参数。

---

## 七、Hyperparameter Tuning（超参数调优）

> 来源：`EE6405_W5_HPT_For Students.pdf` + `Week 8(1).ipynb`。

### 7.1 什么是 Hyperparameter

- **Hyperparameter**：外部配置，影响训练过程和模型性能。控制学习过程，决定学习算法最终学到的 parameter 值。
- 与 model parameter（权重）不同：hyperparameter 是**人为设定**的，不是学出来的。
- 无法预先知道某问题的最佳值——靠 rules of thumb、借鉴其他问题、或 trial and error 搜索。

### 7.2 K-Fold Cross-Validation（K 折交叉验证）

- **Cross-validation**：重采样程序，在有限数据上评估模型。
- 参数 **k** = 数据分成几组。k=10 即 10-fold CV。
- 比 simple train/test split **更不偏、更不乐观**。
- ⚠️ **评估的是模型设计，不是某次训练**——每折都重新训练同一设计的模型。

**步骤**：
1. Shuffle 数据集。
2. 分成 k 组。
3. 每组轮流当 hold-out test set，其余 k-1 组训练 → 评估 → 保留分数 → 丢弃模型。
4. 汇总 k 个分数。

**选 k 的三种策略**：
| 策略 | 含义 |
|---|---|
| **Representative** | 每折足够大，能统计上代表整体 |
| **k=10** | 实验发现低偏差、适中方差 |
| **k=n** | Leave-one-out CV（每折一个样本） |

**notebook 代码**（`Week 8(1).ipynb` cell 4）：

```python
from sklearn.model_selection import GridSearchCV, cross_val_score
param_grid = {'alpha': [0.1, 0.5, 1.0]}
classifier = MultinomialNB()
grid_search = GridSearchCV(classifier, param_grid, cv=5)
grid_search.fit(X, y)
best_classifier = grid_search.best_estimator_
cv_scores = cross_val_score(best_classifier, X, y, cv=5, scoring='f1_macro')
```

- **GridSearchCV**：网格搜索 + CV，`cv=5` 表示 5-fold。
- `best_estimator_`：最优超参对应的模型。
- `cross_val_score`：对最佳模型再做 5-fold CV 评估。
- `cv_results_`：所有组合的详细结果（可转 DataFrame）。

> ⭐ **Week8MCQ Q1**：以下哪个**不**用 5-fold？
> - `GridSearchCV(classifier, param_grid)` —— **未指定 cv**，默认 5-fold（sklearn 默认 cv=5 for classifier）→ 实际会用 5-fold。但题目问"不 split into 5-fold"——需注意 `cross_val_score` 不指定 cv 时行为。
> - 答案需看选项细节：`GridSearchCV(classifier, param_grid)`（无 cv 参数）和 `cross_val_score(best_classifier, X, y, scoring='f1_macro')`（无 cv 参数）行为依版本。本题考"显式 `cv=5`"vs"省略"。

> ⭐ **Week8MCQ Q2**：KFold 的 missing code：
> ```python
> kf = KFold(n_splits=5, shuffle=True, random_state=42)
> for train_index, val_index in kf.split(X):
>     # missing code
> ```
> **答案**：
> ```python
> X_train, y_train = X[train_index], y[train_index]
> X_val, y_val = X[val_index], y[val_index]
> ```
> 干扰项：`X_train, X_val = X[train_index], X[train_index]`（val 也用 train_index）、`X[val_index], X[val_index]`（train 用 val_index）、行列混搭。

### 7.3 Optimizers（优化器）

优化器在训练中调整 model parameter 以最小化 loss function。常见三种：

#### Gradient Descent（梯度下降）
- 一致地修改参数以达到 local minimum：
  $$x_{new} = x - \alpha \nabla f(x)$$
- $\alpha$ 是 step size（学习率）。
- 缺点：数据集大时计算成本高。

#### Stochastic Gradient Descent（SGD）
- 不用整个数据集，每次随机取一个 batch：
  $$w := w - \eta \nabla Q_i(w)$$
- 噪声更大，需更多迭代，但每步更便宜。

#### Adam（Adaptive Moment Estimation）
- SGD 的扩展，**自适应地**为每个参数算个体学习率（基于一阶矩 $m_t$ 和二阶矩 $v_t$）。
- 含 momentum term（累积过去梯度运行平均），帮加速、克服 local minima。
- 含 bias correction（早期迭代偏差修正）。
- 公式：
  $$m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$$
  $$v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$$
  $$w_{t+1} = w_t - \alpha \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$
- $\beta_1, \beta_2$ 是一阶/二阶矩的衰减率，$\epsilon$ 防止除零。

#### RMSprop（Root Mean Square Propagation）
- 保持梯度平方的移动平均，用它归一化梯度：
  $$v(w, t) = \gamma v(w, t-1) + (1-\gamma) \nabla Q_i(w)^2$$
  $$w := w - \frac{\eta}{\sqrt{v(w, t)}} \nabla Q_i(w)$$
- $\gamma$ 是 forgetting factor。
- 振荡大的参数被惩罚更新。

> notebook 中 RNN/LSTM 训练用 `optim.Adam(model.parameters(), lr=0.01)`（cell 11）。

> ⭐ **Week6MCQ Q5**：调 Adam 的 learning rate 哪个可行？
> - `optimizer = optim.Adam(model.parameters(), lr=1e-2)` ✅
> - `optimizer = optim.Adam(model.parameters(), lr=1e-3)` ✅
> - 两者都可行（1e-2 和 1e-3 都是合法学习率）。干扰项用 `eps=`（那是 Adam 的数值稳定参数，不是 learning rate）。
> 答案需看具体选项：题目问"adjust the learning rate"，所以 `lr=` 开头的都对；`eps=` 不调学习率。

### 7.4 Loss Functions（损失函数）

- Loss function 评估算法建模数据的好坏，训练目标是最小化它。
- 选择取决于任务性质（regression / classification）。

#### Binary Cross Entropy（BCE，二元交叉熵）— 二分类
$$\text{BCE}(y, \hat{y}) = -\frac{1}{N} \sum_{i=1}^N [y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i)]$$
- 比较预测概率与实际类（0 或 1），惩罚偏离。
- 负号和除以 N 是算 batch 平均损失。

#### Categorical Cross Entropy（CCE，多类交叉熵）— 多分类
$$\text{CCE}(y, \hat{y}) = -\frac{1}{N} \sum_{i=1}^N \sum_{j=1}^C y_{ij} \log(\hat{y}_{ij})$$
- $C$ = 类别数。常与输出层 **softmax** 搭配。

> notebook 训练用 `criterion = nn.CrossEntropyLoss()`（cell 11）——PyTorch 的 CrossEntropyLoss 内含 softmax，用于多分类。

### 7.5 Batch Size（批大小）

- **Batch size**：一次 iteration 用的训练样本数。
- **大 batch**：权重更新少 → 训练快，但可能精度低；适合 GPU 并行。
- **小 batch**：更新频繁 → 可能更准，但训练慢；适合计算资源有限或 online learning。

### 7.6 Learning Rate（学习率）

- **Learning rate**：优化步长，控制权重更新幅度。
- **过高**：收敛快但可能 overshoot、振荡或发散。
- **过低**：稳定但训练时间长。
- 常见范围 **0.1 ~ 0.0001**；常用 grid search / random search 找最优。

> ⭐ notebook cell 11：`optimizer = optim.Adam(model.parameters(), lr=0.01)`。

### 7.7 Epochs（轮数）

- **Epoch**：完整遍历一次训练数据集。
- 太少 → underfitting；太多 → overfitting。
- **Early Stopping**：验证集性能不再提升时停止训练，防 overfitting。

### 7.8 Early Stopping（早停）

`Week 8(1).ipynb` cell 14 给出 `EarlyStopping` 类：
- 参数：`patience`（容忍几轮不提升）、`delta`（最小改善阈值）、`restore_best_weight`（恢复最佳权重）、`mode='min'`（监控 loss 越小越好）。
- 当 `val_loss` 连续 `patience` 轮不改善 → 停止训练 + 恢复最佳权重。
- 也可用 `ignite.handlers.EarlyStopping`（cell 13）。

### 7.9 Gradient Clipping（梯度裁剪）

- 防止 **exploding gradient**（RNN 中常见），对梯度设阈值。
- 稳定训练，限制梯度幅度。常用阈值 ~1.0。
- 两种方式：
  - **Clipping by value**：把梯度裁剪到 $[-c, c]$。
  - **Clipping by norm**：按梯度范数缩放。

**notebook 代码**（`Week 8(1).ipynb` cell 10）：
```python
torch.nn.utils.clip_grad_value_(model.parameters(), clip_value=0.5)
```

> ⭐ **Week8MCQ Q5**：选正确的 gradient clipping 行：
> **答案**：`torch.nn.utils.clip_grad_value_(model.parameters(), clip_value=0.5)`
> - `clip_value=0.5` 必须是**数值**（float），不是字符串 `'0.5'`。
> - 必须传 `model.parameters()` 作为第一个参数。
> 干扰项：`clip_grad_value_(clip_value=0.5)`（缺 parameters）、`clip_value='0.5'`（字符串类型错）。

> ⭐ **Week8MCQ Q3**：以下代码的作用？
> ```python
> vocab_size = len(vectorizer.get_feature_names_out())
> embedding_dim = 100
> hidden_dim = 128
> output_dim = len(np.unique(y))
> ```
> **答案**：初始化 vocab size 及 embedding/hidden/output 维度，为神经网络模型定义结构。干扰项：只算 feature names 长度（片面）、只算 unique classes（片面）。

> ⭐ **Week8MCQ Q4**：以下代码的作用？
> ```python
> X_train_tensor = torch.tensor(X_train.toarray(), dtype=torch.long)
> y_train_tensor = torch.tensor(y_train, dtype=torch.long)
> train_data = TensorDataset(X_train_tensor, y_train_tensor)
> train_loader = DataLoader(train_data, batch_size=4)
> model = LSTMClassifier(vocab_size, embedding_dim, hidden_dim, output_dim)
> ```
> **答案**：把训练/验证数据转 PyTorch tensor，建 DataLoader，初始化 LSTM classifier。干扰项：normalize/augmentation（没做）、feature selection（没做）、"trains"（这段只初始化，没训练循环）。

---

## 八、Training a Neural Network（notebook 完整训练循环）

`Week 6.ipynb` cell 11 给出 RNN 的完整训练循环：

```python
model = RNNModel(vocab_size, embedding_dim, hidden_dim, vocab_size)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(num_epochs):
    model.train()                # 训练模式
    optimizer.zero_grad()        # 清梯度（⭐ Week6MCQ Q4）
    output = model(sequence_data)            # forward
    loss = criterion(output.view(-1, vocab_size), target_data.view(-1))  # 算 loss
    loss.backward()              # backward
    optimizer.step()             # 更新权重
    if (epoch + 1) % 2 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
```

### 8.1 关键步骤

| 步骤 | 代码 | 作用 |
|---|---|---|
| **训练模式** | `model.train()` | 启用 dropout/batchnorm 等训练行为 |
| **清梯度** | `optimizer.zero_grad()` | 清空上一步梯度（⭐ Q4） |
| **Forward** | `output = model(x)` | 前向算预测 |
| **算 loss** | `criterion(output, target)` | 计算损失 |
| **Backward** | `loss.backward()` | 反向传播算梯度 |
| **更新** | `optimizer.step()` | 按 optimizer 规则更新权重 |

> ⭐ **Week6MCQ Q4**：`optimizer.zero_grad()` 的作用？
> **答案**：It clears the gradients of all optimized tensors before the backward pass.（在 backward 前清除所有优化张量的梯度）。
> 干扰项：initialize weights（初始化是 `__init__` 做）、calculate loss（那是 `criterion`）、update parameters（那是 `optimizer.step()`）、set evaluation mode（那是 `model.eval()`）。

### 8.2 GPU 加速与评估模式（cell 12–14）

- `torch.cuda.is_available()` 检查 GPU。
- `model.cuda()` 把模型移到 GPU；输入 tensor 也加 `.cuda()`。
- `model.train()` / `model.eval()` 切换训练/评估模式——eval 时关闭 dropout/batchnorm。

### 8.3 `output.view(-1, vocab_size)` 的 reshape

- `criterion = nn.CrossEntropyLoss()` 期望输入 shape `(N, C)`：N 是样本数，C 是类别数。
- RNN 输出 `(batch, seq, output_size)` → `view(-1, vocab_size)` 拉平成 `(batch*seq, vocab_size)`。
- `target_data.view(-1)` 同样拉平成 `(batch*seq,)`。

---

## 九、Week 5 tasks（课堂任务要点）

`Week 5 tasks.pdf`——team discussion prompts：

1. **RNN vs LSTM vs GRU 选择**：何时用 vanilla RNN 而非 LSTM？GRU vs LSTM？
   - 答：短序列/资源紧 → RNN/GRU；长序列/长依赖 → LSTM；折中 → GRU（参数少、接近 LSTM 效果）。
2. 选一个适合 LSTM 或 GRU 的 NLP 问题（classification/translation/summarization）。
3. 用常见数据集（Reuters news classification / IMDB reviews）。
4. **从 7 个超参中选 3 个探索**（可用 PyTorch 替代 Keras）。
5. 调高/中/低或不同类型（learning rate、batch size、optimizer、loss function），解释对下游任务的影响，画图。
6. 用"不合适"的超参值/类型会发生什么？
- 参考：gradient clipping、cross-validation、regularization、optimizer。

> 这 7 个超参对应 §七：optimizer、loss function、batch size、learning rate、epochs、gradient clipping、regularization。

---

## 十、考点速查表（Week 5 MCQ 汇总）

| 来源 | 题 | 考点 | 答案要点 |
|---|---|---|---|
| **Week6MCQ Q1** | `self.embedding` 作用 | indices → dense vector representations | 干扰：fc 的作用、hidden state 初始化 |
| **Week6MCQ Q2** | RNN → bidirectional | `bidirectional=True` + `fc=hidden_dim*2` | 必须同时改两处 |
| **Week6MCQ Q3** | RNN → LSTM | `nn.RNN` → `nn.LSTM` | 只换类名，不动 fc |
| **Week6MCQ Q4** | `optimizer.zero_grad()` 作用 | clears gradients before backward | 不是 init/calc/update/eval mode |
| **Week6MCQ Q5** | 调 Adam learning rate | `lr=1e-2` / `lr=1e-3` | `eps=` 不是 learning rate |
| **Week8MCQ Q1** | 哪个不用 5-fold | 看 `cv=5` 是否显式 | GridSearchCV/cross_val_score 的 cv 参数 |
| **Week8MCQ Q2** | KFold missing code | `X[train_index], X[val_index]` | 行列不混搭 |
| **Week8MCQ Q3** | 维度定义代码作用 | 初始化 NN 结构维度 | 不只是算 feature 长度 |
| **Week8MCQ Q4** | tensor + DataLoader 代码 | 转 tensor + DataLoader + 初始化 LSTM | 不含 normalize/augment/train |
| **Week8MCQ Q5** | gradient clipping 正确写法 | `clip_grad_value_(model.parameters(), clip_value=0.5)` | clip_value 是 float 不是 string |

---

## 十一、本周要点小结

- **Sequential data** 需要记忆和顺序敏感的模型，传统 feedforward 网络有 lack of memory / order insensitivity / variable-length limitation 三大局限。
- **RNN**：hidden state $h_t = g(x_t, h_{t-1})$ 记忆历史；参数跨时间步共享；vanilla RNN 用 $\tanh(Ux_t + Wh_{t-1} + b)$；但受 vanishing/exploding gradient 困扰。
- **LSTM**：cell state + 三道 gate（forget/input/output）解 vanishing gradient；$c_t = f_t c_{t-1} + i_t \tilde{c}_t$，$h_t = o_t \tanh(c_t)$。
- **GRU**：LSTM 简化版，无 cell state，reset gate + update gate，更省算力。
- **Bi-RNN**：正反向两个 RNN，`bidirectional=True` + `fc` 输入 `hidden_dim*2`；适合需未来上下文的任务（NER/POS）。
- **Hyperparameter Tuning**：K-Fold CV 评估模型设计；GridSearchCV 网格搜索；optimizer（SGD/Adam/RMSprop）；loss（BCE/CCE）；batch size、learning rate、epochs、early stopping、gradient clipping 都是可调超参。
- **训练循环**：`train() → zero_grad() → forward → loss → backward → step()`；`zero_grad()` 清梯度、`step()` 更新权重。
- **PyTorch API**：`nn.Embedding`/`nn.RNN`/`nn.LSTM`/`nn.GRU`（接口一致，换类名）；`optim.Adam(lr=...)`；`clip_grad_value_(parameters, clip_value)`；`CrossEntropyLoss`（内含 softmax）。

---

## 十二、必背 API/参数表

| API | 精确写法 | 易错 |
|---|---|---|
| Embedding | `nn.Embedding(vocab_size, embedding_dim)` | 作用：indices → dense vector |
| RNN | `nn.RNN(embedding_dim, hidden_dim, batch_first=True)` | `batch_first=True` |
| LSTM | `nn.LSTM(embedding_dim, hidden_dim, batch_first=True)` | 与 RNN 接口一致 |
| GRU | `nn.GRU(embedding_dim, hidden_dim, batch_first=True)` | 同上 |
| Bi-RNN | `nn.RNN(..., bidirectional=True)` + `fc=nn.Linear(hidden_dim*2, ...)` | 必须同时改两处 |
| 训练循环 | `train()→zero_grad()→forward→loss→backward()→step()` | zero_grad 在 backward 前 |
| optimizer | `optim.Adam(model.parameters(), lr=0.01)` | lr 调学习率；eps 不是 |
| loss | `nn.CrossEntropyLoss()` | 内含 softmax，多分类 |
| gradient clipping | `torch.nn.utils.clip_grad_value_(model.parameters(), clip_value=0.5)` | clip_value 是 float 不是 string |
| KFold | `KFold(n_splits=5, shuffle=True, random_state=42)` | split 返回 (train_index, val_index) |
| GridSearchCV | `GridSearchCV(classifier, param_grid, cv=5)` | `best_estimator_` 取最佳模型 |
| cross_val_score | `cross_val_score(model, X, y, cv=5, scoring='f1_macro')` | cv 指定 fold 数 |
| 模式切换 | `model.train()` / `model.eval()` | eval 关 dropout/batchnorm |

---

> **下周（Week 6）预告**：进入 **Transformer 与 Attention 机制**（课件已预告 "To be covered next week"），从 RNN/LSTM 转向 self-attention 架构。同时本周有 **IRA/TRA #2**（20 分钟，多选多答，扣分制，覆盖 Week 5 + Week 6）。
>
> **笔记约定补充**：本周新增保留英文术语（sequential data, RNN, hidden state, vanilla RNN, parameter sharing / tied parameters, sequence-to-one / one-to-sequence / sequence-to-sequence, sigmoid, tanh, vanishing gradient, exploding gradient, LSTM, cell state, forget gate, input gate, output gate, GRU, reset gate, update gate, Bi-RNN, bidirectional, hyperparameter, K-fold cross-validation, GridSearchCV, cross_val_score, optimizer, Gradient Descent, SGD, Adam, RMSprop, momentum, bias correction, Binary Cross Entropy, Categorical Cross Entropy, softmax, batch size, learning rate, epoch, early stopping, gradient clipping, clipping by value / by norm, nn.Embedding, nn.RNN, nn.LSTM, nn.GRU, optimizer.zero_grad, optimizer.step, model.train/eval 等）。中文用于组织句意与补充释义。
>
> **说明**：本周无录播转写，以上为基于课件/notebook/MCQ/tasks 整理。Neural Language Models 课件署名 Dr. Simon Liu，HPT 课件署名 Dr. S. Supraja。若后续补录播，可补充老师口述要点。
