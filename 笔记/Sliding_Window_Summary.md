# 📘 滑动窗口题型总结（MLE / 推荐算法方向专用）

## 🧠 一、核心思想

> 滑动窗口（Sliding Window）是一种用两个指针维护动态区间 `[left, right]`
> 的方法，用于高效处理**连续子数组 / 子串问题**。
>
> **本质：**
> 动态维护窗口内的状态，使得每次扩张或收缩都只处理一个元素，从而实现
> `O(n)` 的线性复杂度。

------------------------------------------------------------------------

## 🧩 二、通用模板（举一反三）

``` python
def sliding_window(arr):
    left = 0
    window = defaultdict(int)   # 记录窗口中元素出现情况
    res = 0                     # 存结果（长度、数量、最大值等）

    for right in range(len(arr)):
        # 1️⃣ 扩展窗口：加入新元素
        x = arr[right]
        window[x] += 1

        # 2️⃣ 判断是否需要收缩窗口
        while not valid(window):
            y = arr[left]
            window[y] -= 1
            if window[y] == 0:
                del window[y]
            left += 1

        # 3️⃣ 在满足条件时更新结果
        res = update(res, window)

    return res
```

📌 模板中可以灵活修改： -
`valid(window)`：判断窗口是否满足条件（长度、和、无重复等）\
- `update(res, window)`：根据问题更新结果（最大长度、最短区间、计数等）

------------------------------------------------------------------------

## ⚙️ 三、典型题型分类

### 1️⃣ 固定窗口类（窗口大小固定）

📘 **代表题：** - 滑动窗口最大值（LeetCode 239） - 平均温度、连续 K
天的最大销售额等问题

**思路：** 窗口大小固定为
`k`，每次右移一格，维护窗口内的最大值/平均值等。

``` python
from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    res = []
    for i, num in enumerate(nums):
        # 移除不在窗口范围内的下标
        while dq and dq[0] <= i - k:
            dq.popleft()
        # 移除比当前数小的（保持递减）
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        # 窗口形成后记录结果
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
```

🔹 **举一反三（推荐系统场景）**\
👉 计算"过去 7 天内用户点击率（CTR）滑动平均值"\
👉 监控"最近 N 次曝光的点击趋势变化"

------------------------------------------------------------------------

### 2️⃣ 动态窗口类（窗口大小可变）

📘 **代表题：** - 无重复字符的最长子串（LeetCode 3） - 和小于 K
的最短子数组（LeetCode 209） - 至少包含 K 个不同数字的子数组

``` python
def lengthOfLongestSubstring(s):
    left = 0
    seen = set()
    max_len = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        max_len = max(max_len, right - left + 1)
    return max_len
```

🔹 **举一反三（推荐系统场景）**\
👉 模拟用户 session：最长连续不重复浏览的商品序列\
👉 计算时间窗口内的曝光多样性（distinct item count）

------------------------------------------------------------------------

### 3️⃣ 满足条件的窗口（统计类）

📘 **代表题：** - 最小覆盖子串（LeetCode 76） - 和为 K
的子数组数目（LeetCode 560）

``` python
def minWindow(s, t):
    need = Counter(t)
    window = defaultdict(int)
    have, need_count = 0, len(need)
    left, res = 0, (0, float('inf'))
    
    for right, c in enumerate(s):
        window[c] += 1
        if c in need and window[c] == need[c]:
            have += 1
        while have == need_count:
            if right - left < res[1] - res[0]:
                res = (left, right)
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1
    l, r = res
    return "" if res[1] == float('inf') else s[l:r+1]
```

🔹 **举一反三（推荐系统场景）** 👉
找出包含所有兴趣标签的最短用户浏览序列\
👉 识别用户在 session 中首次触发"点击+加购+下单"全流程的最短时间窗口

------------------------------------------------------------------------

### 4️⃣ 累积和窗口（前缀和 + 滑动窗口）

📘 **代表题：** - 和为 K 的子数组数（LeetCode 560） -
平均值小于阈值的最短窗口

``` python
def subarraySum(nums, k):
    prefix = 0
    count = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
```

🔹 **举一反三（推荐系统场景）** 👉 统计"近 N 次曝光中累计转化 = k
的次数"\
👉 分析"时间窗口内 engagement 总和恰好达到某阈值的行为段落"

------------------------------------------------------------------------

## 🧮 四、时间复杂度总结

  操作类型           均摊复杂度   说明
  ------------------ ------------ -------------------------
  窗口右移（扩张）   O(1)         每个元素仅进入一次
  窗口左移（收缩）   O(1)         每个元素仅退出一次
  总复杂度           O(n)         相较暴力 O(n²) 极大优化

------------------------------------------------------------------------

## 💬 五、推荐算法中的"滑动窗口思维"

  应用场景                           滑动窗口作用
  ---------------------------------- ------------------------------------
  **用户行为序列建模**               提取最近 N 次点击行为作为序列输入
  **Session-based Recommendation**   定义时间窗口内的用户活跃会话
  **实时特征统计**                   计算滑动 CTR、曝光率、召回率等特征
  **异常检测**                       检测在滑动时间窗口内的行为突变
  **时间序列建模**                   用固定长度窗口构造 LSTM 输入序列

------------------------------------------------------------------------

## ✅ 六、一句话记忆模板

> **滑动窗口三步走：** 1️⃣ **扩张窗口** → 把右指针加进来\
> 2️⃣ **收缩窗口** → 当不满足条件时移动左指针\
> 3️⃣ **更新结果** → 当满足条件时记录答案
