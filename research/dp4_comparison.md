# 次数 4 の比較ノート

日付: 2026-11-20 (JST) / 版: 1.0

## 位置づけと主張の状態

次数 1・2 の分類がどこまで次数 4 に共通し、どこから変わるかを理解するためのノートである。次数 4 の詳細な分類・計算を進める正本は [poisson-22ci](https://github.com/uedakazushi/poisson-22ci) と [nc-22ci](https://github.com/uedakazushi/nc-22ci) にある。本リポジトリの次数 1・2 の論文から独立に、比較に必要な数学と再取得しにくい明示公式を保持する。

出発資料は『次数1・2・4のdel Pezzo manifold上のPoisson構造と非可換幾何：分類・ambientへの持ち上げ・超曲面と完全交叉の量子化』、2026-11-11、版 2.0、§§10–16。以下はその数学を現在の比較目的に沿って整理したものである。旧資料自体を読むことを再開の前提としない。

**確認範囲。** 下記の証明は現行ノートに記載したが、次数 4 全体を今回独立に全面監査したという意味ではない。Donagi の同時対角化と Smith–Stafford の Corollary 3.9・Theorems 5.4–5.5 は一次本文の対応箇所を照合したが、Smith–Stafford のスキャン中の中心元係数は今回画像として再確認できていないため、下記の係数表示は出発資料とその変数変換の計算に基づく。座標式、rank 4 の block 構成、Euler 方向による rank の判定、ambient lift の非一意例、Sklyanin の変数変換と中心元の係数は今回読み直して確認した。大域的微分形式の同型、Jacobiator の持ち上げ、一般の formality 入力、AS 正則性に用いる既知定理、Sklyanin 文献の全仮定の独立監査は残る。次数 4 に対しては、次数 1・2 の論文で今回証明した **Jacobi ideal の scheme としての一致**を自動的に主張しない。新規性は未判定である。

## 1. 設定と比較の要点

基礎体は $\mathbb C$。$X$ は滑らかな連結 $n$ 次元 del Pezzo manifold、$n\ge2$、$-K_X=(n-1)H$、$H^n=4$ とする。標準モデルは

$$
X=V(Q_0,Q_1)\subset\mathbb P(V)=\mathbb P^{n+2},\qquad
N=\dim V=n+3,\qquad S=\operatorname{Sym}(V^*).
$$

二次式の pencil の判別式が相異なる $N$ 個の根を持つことと $X$ の滑らかさは同値である。非退化な二つの pencil member と座標を選び、

$$
Q_0=\frac12\sum_{i=1}^N x_i^2,\qquad
Q_1=\frac12\sum_{i=1}^N\lambda_i x_i^2,
\qquad\lambda_i\ne\lambda_j\ (i\ne j),\quad \lambda_i\ne0
$$

とできる。最後の条件は $Q_1$ に $Q_0$ の定数倍を加えて実現できる。$e_i=\partial_{x_i}$、$\Delta_{ij}=\lambda_j-\lambda_i$ とする。

| 項目 | 次数 1・2 | 次数 4 |
|---|---|---|
| 標準モデル | 重み 6 または 4 の超曲面 | 通常の射影空間内の $(2,2)$ 完全交叉 |
| 大域的二重ベクトルの次元 | $n$, $\binom{n+1}{2}$ | $\binom{n+3}{4}$ |
| Poisson 条件 | 零 ideal、または Plücker ideal | 下記の座標 Jacobi 方程式 |
| ambient lift | スタック上で一意 | 存在するが通常は非一意 |
| cone 上の正規化 | $F$ を Casimir とする | $Q_0,Q_1$ をともに Casimir とする。この条件下では一意 |
| 非零構造の一般階数 | 常に 2 | 分解可能な族は 2。$n\ge5$ には rank 4 の構造 |
| 量子化後の定義式 | 中心的非零因子一個 | 中心的二次正則列二個 |

## 2. 全二重ベクトルと二つの Casimir

順序付き定義式 $(Q_0,Q_1)$ を固定すると、資料内で証明されている線型同型は

$$
\Lambda^4 V\xrightarrow{\sim}H^0(X,\Lambda^2T_X),\qquad C\longmapsto\pi_C.
$$

対応する homogeneous quadratic bivector は

$$
B_C=\iota_{\mathrm dQ_1}\iota_{\mathrm dQ_0}C,
\qquad
\{f,g\}_C=C(\mathrm dQ_0,\mathrm dQ_1,\mathrm df,\mathrm dg).
\tag{2.1}
$$

$Q_0,Q_1$ はともに Casimir である。$C=\sum_{i<j<k<\ell}c_{ijk\ell}e_i\wedge e_j\wedge e_k\wedge e_\ell$ とし、係数を全添字に交代的に拡張すると

$$
P_C^{ij}(x):=\{x_i,x_j\}_C
=\sum_{a<b}\Delta_{ab}c_{ijab}x_ax_b.
\tag{2.2}
$$

添字が重なる $c$ は零とする。特に $\sum_i\partial_{x_i}P_C^{ij}=0$ で、ambient の標準体積形式について発散が零である。

### 大域的同型の証明

$r=n-2$ とおく。随伴公式は $\Lambda^2T_X\simeq\Omega_X^r(r+1)$ を与える。必要な同型は

$$
\Lambda^{r+1}V^*\xrightarrow{\sim}H^0(X,\Omega_X^r(r+1)),\qquad
\eta\longmapsto\iota_E\eta,
\quad E=\sum_i x_i\partial_{x_i}.
\tag{2.3}
$$

$R_0=S/(Q_0,Q_1)$、$U=\operatorname{Spec}R_0\setminus\{0\}$ とする。$R_0$ は次元 $n+1$ の Cohen–Macaulay 環なので、頂点での局所コホモロジーから

$$
H^0(U,\mathcal O_U)=R_0,\qquad H^q(U,\mathcal O_U)=0\quad(1\le q\le n-1)
$$

を得る。滑らかな $U$ の conormal 列

$$
0\longrightarrow\mathcal O_U^{\oplus2}
\xrightarrow{(\mathrm dQ_0,\mathrm dQ_1)}V^*\otimes\mathcal O_U
\longrightarrow\Omega_U^1\longrightarrow0
$$

では、左辺の生成元に重み 2、$\mathrm dx_i$ に重み 1 を与える。その外積解像度において、$\Omega_U^k$ を解像する第 $j$ 項は

$$
\operatorname{Sym}^j(\mathbb C^2)\otimes\Lambda^{k-j}V^*\otimes\mathcal O_U
\qquad(0\le j\le k)
$$

で生成元の重みは $k+j$。$k\le n-1$ では上の消滅により大域切断の右端まで完全である。従って、重み $k$ の $k$ 形式は定数形式から一意に来る。重み $k+1$ の $k$ 形式は線型係数の ambient 形式で表され、その曖昧さは

$$
\mathrm dQ_0\wedge\gamma_0+\mathrm dQ_1\wedge\gamma_1,
\qquad\gamma_a\in\Lambda^{k-1}V^*.
$$

$U\to X$ は $\mathbb G_m$-torsor なので、(2.3) の右辺は $U$ 上の重み $r+1$ の水平 $r$ 形式である。線型係数の ambient 代表を $\widehat\alpha$ とすると、$\mathrm d\widehat\alpha$ は代表によらない定数 $(r+1)$ 形式である。Cartan の公式

$$
(r+1)\alpha=\mathcal L_E\alpha
=\iota_E\mathrm d\alpha+\mathrm d\iota_E\alpha
=\iota_E(\mathrm d\widehat\alpha|_U)
$$

から全射性を得る。定数形式 $\eta$ が $\iota_E\eta|_U=0$ を満たせば、その微分から $(r+1)\eta|_U=0$ となり、重み $r+1$ の $(r+1)$ 形式への定数形式の単射性により $\eta=0$。これで同型になる。

体積形式 $\mathrm{vol}=\mathrm dx_1\wedge\cdots\wedge\mathrm dx_N$ を選び、$\eta=\iota_C\mathrm{vol}$ と置く。穿孔 cone の residue 体積形式

$$
\nu=\operatorname{Res}_{Q_0=Q_1=0}\frac{\mathrm{vol}}{Q_0Q_1},
\qquad \mathcal L_E\nu=(N-4)\nu=(n-1)\nu
$$

について、非零な Jacobian 小行列式を使った局所式から
$\iota_{B_C|_U}\nu=(\iota_C\mathrm{vol})|_U$（向きの規約に伴う全体符号を固定）を得る。さらに $E$ で縮約すると (2.3) となり、(2.1) と大域的同型が一致する。

### 正規化された代表の一意性

斉次二次係数の bivector $B$ が $\iota_{\mathrm dQ_0}B=\iota_{\mathrm dQ_1}B=0$ を満たすとする。固定した $j$ について

$$
\sum_i x_i B^{ij}=0,\qquad\sum_i\lambda_i x_iB^{ij}=0.
$$

三次単項式を比較すると平方項および添字 $i,j$ を含む項が消え、$B^{ij}$ は $i,j,a,b$ がすべて異なる $x_ax_b$ のみを持つ。その係数 $b_{ij;ab}=b_{ij;ba}$ は

$$
b_{ij;ab}+b_{aj;ib}+b_{bj;ia}=0,
\qquad
\lambda_i b_{ij;ab}+\lambda_a b_{aj;ib}+\lambda_b b_{bj;ia}=0.
$$

各四添字集合について、この二本の式と $b_{ji;ab}=-b_{ij;ab}$ を解く。$\lambda_i$ が相異なるため解は一つの係数で決まり、
$b_{ij;ab}=\Delta_{ab}c_{ijab}$、$c$ は全交代、となる。逆にこの形はすべての式を満たす。よって (2.2) が唯一の形である。

順序付き定義式を $M(Q_0,Q_1)$ に変えると、同じ $C$ による括弧は $\det M$ 倍になる。この選択依存性を、内在的な bivector 自体の曖昧さと混同しない。

## 3. Jacobi 方程式と射影化

$J=\tfrac12[B_C,B_C]$ とする。資料内の重要な主張は

$$
[\pi_C,\pi_C]=0\quad\Longleftrightarrow\quad[B_C,B_C]=0\text{ in }S
\tag{3.1}
$$

である。従って intrinsic Poisson 構造はすべて ambient に持ち上がる。

### (3.1) の証明の所在をこのノート内で完結させる

各 $Q_a$ は Casimir なので $\iota_{\mathrm dQ_a}J=0$。$J$ の重みは 0、係数は三次式である。上の residue 表示により $B_C|_U$ の $\nu$ に関する発散は零。発散作用素が Schouten 括弧について次数 $-1$ の導分であることから、$\omega=\iota_{J|_U}\nu$ は閉形式となる。射影化した Jacobiator が零なら $E\wedge J|_U=0$、従って $\iota_E\omega=0$。Euler 重みと Cartan の公式から

$$
(n-1)\omega=\mathcal L_E\omega
=\mathrm d\iota_E\omega+\iota_E\mathrm d\omega=0.
$$

$n\ge2$ なので $J|_U=0$。$R_0$ は整域で $U$ は cone に稠密だから、

$$
J=Q_0U_0+Q_1U_1
$$

と書ける。$U_0,U_1$ は線型係数の三重ベクトル。$\mathrm dQ_0$ で縮約して二つの二次式の互いに素であることを使うと

$$
\iota_{\mathrm dQ_0}U_0=Q_1A,\qquad
\iota_{\mathrm dQ_0}U_1=-Q_0A
$$

となる定数二重ベクトル $A$ がある。さらに縮約して $\iota_{\mathrm dQ_0}A=0$、$Q_0$ の非退化性から $A=0$。$Q_1$ についても同じ議論を行い、$\iota_{\mathrm dQ_a}U_b=0$ を得る。

線型係数の多重ベクトル $U$ がこの二つの縮約で零になるなら $U=0$ である。残りの添字を固定し $U^{iI}=\sum_\ell u_{i;\ell}x_\ell$ と書くと、$x_i^2$ の係数で $u_{i;i}=0$、$x_ix_\ell$ の係数で

$$
u_{i;\ell}+u_{\ell;i}=0,\qquad
\lambda_i u_{i;\ell}+\lambda_\ell u_{\ell;i}=0
$$

となるためである。よって $U_0=U_1=0$、$J=0$。逆は制限と商への降下である。

### 再現可能な座標方程式

$i<j<k$ に対して

$$
J_C^{ijk}(x)=\sum_{\ell=1}^N
\bigl(P_C^{i\ell}\partial_{x_\ell}P_C^{jk}
+P_C^{j\ell}\partial_{x_\ell}P_C^{ki}
+P_C^{k\ell}\partial_{x_\ell}P_C^{ij}\bigr)
\tag{3.2}
$$

とする。展開形は

$$
J_C^{ijk}
=\sum_{\substack{1\le\ell,r\le N\\1\le a<b\le N}}
\Delta_{ab}\Delta_{\ell r}
\bigl(c_{i\ell ab}c_{jk\ell r}
+c_{j\ell ab}c_{ki\ell r}
+c_{k\ell ab}c_{ij\ell r}\bigr)x_ax_bx_r.
\tag{3.3}
$$

すべての三次単項式の係数を零とする。これは $c_{ijk\ell}$ に関する斉次二次方程式であり、(3.1) により Poisson 条件の必要十分な記述となる。**$(Q_0,Q_1)$ による剰余だけを計算する必要はない。** 一方、intrinsic Jacobi scheme とこの表示の scheme としての一致を、本ノートでは独立に結論していない。

## 4. Grassmann 型の族と高階数の障害

非零の分解可能な $C$ が張る四次元部分空間を $A\subset V$ とし、$W=A^\perp$ の基底を $s_1,\ldots,s_{n-1}$ とする。残る四変数を $u_1,\ldots,u_4$ とすると、定数因子を除いて

$$
\{f,g\}_C=\det\frac{\partial(Q_0,Q_1,f,g)}
{\partial(u_1,u_2,u_3,u_4)},\qquad\{s_i,-\}=0.
\tag{4.1}
$$

横断座標の微分が独立な開集合では二次元の葉に接する bivector なので Jacobi が成り立ち、非零の場合にはこの集合が稠密だから多項式恒等式として成り立つ。一般階数は 2。定数倍を除いたこの族は

$$
\operatorname{Gr}(4,V)\simeq\operatorname{Gr}(n-1,H^0(X,H)).
$$

$X\dashrightarrow\mathbb P(W^*)$ の一般ファイバーの稠密開部分が二次元の葉になる。一般の $W$ と一般のファイバーについて、その閉包は $n-2$ 個の $H$ による切断で、Bertini と随伴公式により滑らかな次数 4 の del Pezzo 曲面となる。特殊な $W$ では特異切断や固定成分の除去があり、同じ滑らかさ・完全交叉の主張はしない。

### 低次元

- $n=2$: $\Lambda^2T_X=-K_X=H$ なので全 bivector が Poisson。$\operatorname{Pois}(X)\simeq\mathbb A^5$、射影化は $\mathbb P^4$、すべて相互 compatible。固定した体積形式のもとで $s\in H^0(X,H)$ の括弧は

  $$
  \{f,g\}_s=\det\frac{\partial(Q_0,Q_1,s,f,g)}{\partial(x_1,\ldots,x_5)}.
  \tag{4.2}
  $$

- $n=3$: 被約 Poisson 空間は $\operatorname{Gr}(4,6)\simeq\operatorname{Gr}(2,6)$ のアフィン錐で、次元 9、射影化の次元 8。これは三次元の LPT の既知分類を入力とする。Lefschetz により $\operatorname{Pic}(X)=\mathbb ZH$、$-K_X=2H$。LPT の既約性と一般構造が $H$ の pencil から生じることを使い、閉な Plücker 錐が一般点を含むので全体と一致する。LPT の定理を高次元へそのまま適用してはいけない。
- $n=4$: bivector 空間の次元は $\binom74=35$。このノートは (3.3) を与えるに留まり、全成分の列挙は主張しない。

### $n\ge5$ の rank 4 の具体例

$N\ge8$ とし

$$
C=e_1\wedge e_2\wedge e_3\wedge e_4
+e_5\wedge e_6\wedge e_7\wedge e_8.
\tag{4.3}
$$

$A=\{1,2,3,4\}$、$B=\{5,6,7,8\}$ とする。対応する括弧は二つの四変数 Jacobian 括弧の和であり、異なる block の係数と微分方向が交わらないため相互 Schouten 括弧が零。各 block の十分多くの座標が非零なら、相異なる $\lambda_i$ により各 rank は 2 で和の rank は 4。

この開集合は cone と交わる。実際、$y_i=x_i^2$ とおけば cone の条件は
$\sum_i y_i=\sum_i\lambda_i y_i=0$。この線型解空間はどの座標超平面にも含まれないので、有限個の座標超平面を避けた解を取り平方根を選べる。

射影化で rank が落ちないことを別に確認する。$Q_{0,A}=\frac12\sum_{i\in A}x_i^2$ は和の括弧の Casimir だが cone 上で恒等的には零でない。もし零なら次数 2 の成分で $Q_{0,A}\in\langle Q_0,Q_1\rangle$。$B$-block の相異なる四つの $\lambda_i$ の係数を比較するとその線型結合の係数はともに零となり矛盾する。よって一般点で

$$
E(Q_{0,A})=2Q_{0,A}\ne0.
$$

Hamiltonian 方向は $Q_{0,A}$ を消すので $E$ は bivector の像に入らない。Euler 方向で商を取ってもその四次元の像は単射に写り、$X$ 上の一般階数も 4 である。従って、次数 1・2 の「すべて rank 2 で Grassmann 型」という結論は次数 4 の全次元へ拡張できない。

## 5. Ambient lift が一意でない具体的理由

定数ベクトル $v,w\in V$ に対して $Q_0v\wedge w$ は Poisson で、$X$ 上への制限は零である。二次元の定数可積分分布の bivector の任意の関数倍は Poisson になるからである。一般の $v,w$ では $E\wedge Q_0v\wedge w\ne0$ なので射影空間上でも非零。

非零構造についても、$n\ge3$ で $C=e_1\wedge\cdots\wedge e_4$ とすると

$$
B_C+tQ_0e_5\wedge e_6\qquad(t\in\mathbb C)
\tag{5.1}
$$

は同じ $\pi_C$ を持ち上げる互いに異なる Poisson 構造である。$B_C$ は最初の四変数のみに依存し、$Q_0$ はその Casimir なので混合 Schouten 括弧が零になる。追加項は一般に $Q_1$ を Casimir としない。従って二つの Casimir を保つ代表の一意性とは矛盾しない。

## 6. 次数 4 の曲面の退化因子

この節は $n=2$。$s\ne0$ に対応する Poisson 構造の零因子は
$D_s=X\cap(s=0)\subset\mathbb P^3$ で、$(2,2)$ 完全交叉、$p_a(D_s)=1$。$X\setminus D_s$ は二次元の symplectic leaf、$D_s$ の各点は零次元の leaf である。

すべての $D_s$ は被約であり、可能な型は次表に限られる。各固定 $X$ で全型が現れるという意味ではない。

| 成分次数 | 型 |
|---|---|
| 4 | 滑らかな楕円曲線、または node / cusp を一個持つ既約有理曲線 |
| 3+1 | 滑らかな有理三次曲線と直線。二点で横断的に交わるか、一点で交点重複度 2 |
| 2+2 | 滑らかな平面二次曲線二本。二点で横断的に交わるか、一点で交点重複度 2 |
| 2+1+1 | 滑らかな二次曲線と直線二本。三つの相異なる node、または通常三重点一個 |
| 1+1+1+1 | 直線四本の四角形。隣接する直線だけが横断的に交わる |

**被約性。** 重複成分 $C$ の次数 $d_C=H\cdot C$ は正整数で $2d_C\le4$。$d_C=2$ なら $D_s=2C$ で $C^2=1$、$H\cdot C=2$ となり、随伴公式の偶奇に反する。$d_C=1$ なら $C$ は直線 $L$、$L^2=-1$。$D_s=mL+R$、$m\ge2$ と書くと $L\cdot R=m+1$、$H\cdot R=4-m$。$L$ を含み $R$ の成分を含まない hyperplane section を選ぶと、その残余の有効因子から $L\cdot R\le H\cdot R$。これは $m+1\le4-m$ となり矛盾する。

**成分と交点。** 既約なら算術種数 1 と滑らかな曲面上の曲線であることから表の第一行になる。可約な場合、各成分は $1\le d_C\le3$ を満たし、Hodge 指数定理と随伴公式から

$$
d_C-2\le C^2\le d_C^2/4,
\qquad C^2-d_C\equiv0\pmod2.
$$

よって $(d_C,C^2)=(1,-1),(2,0),(3,1)$。いずれも $p_a(C)=0$ なので滑らかな有理曲線であり、埋め込み次数により直線、平面二次曲線、twisted cubic となる。

$3+1$ と $2+2$ は二成分の交点数が 2。$2+1+1$ では二次曲線 $C$、二直線 $L_1,L_2$ に対して $D_s\cdot C=2$、$D_s\cdot L_i=1$ から各組の交点数が 1 となる。従って三つの node または異なる三接線を持つ通常三重点。四直線の場合は各直線が他と合計二回交わり、異なる射影直線の局所交点重複度は高々 1 なので、交点グラフは四頂点の単純な 2-正則グラフ、すなわち四角形である。三本が一点に集まるとその三本だけで交点数を使い切り第四の直線の条件に反する。

一般の $s$ は Bertini により滑らかな楕円曲線を与える。特異因子を与える超平面は $X$ の双対多様体であり、$Q_0,Q_1,s$ の Jacobian の rank 低下で調べられる。これは $\mathbb P^4$ 上の退化型の層別であって、別の Poisson 成分の主張ではない。

## 7. 二つの中心元による形式量子化

$R=\mathbb C[[\hbar]]$、$\deg\hbar=0$ とする。資料の主張は、任意の $\pi_C$ について次数付き形式量子化 $A_\hbar$ と中心的二次正則列 $\Omega_{0,\hbar},\Omega_{1,\hbar}$ を選べるというものである。

$$
A_\hbar/\hbar A_\hbar\simeq S,\qquad
\Omega_{a,\hbar}=Q_a+O(\hbar),\qquad
B_\hbar=A_\hbar/(\Omega_{0,\hbar},\Omega_{1,\hbar}).
\tag{7.1}
$$

$B_\hbar$ の各内部次数は有限自由 $R$ 加群であり、

$$
H_{A_\hbar}(t)=\frac1{(1-t)^{n+3}},\qquad
H_{B_\hbar}(t)=\frac{(1-t^2)^2}{(1-t)^{n+3}}
=\frac{(1+t)^2}{(1-t)^{n+1}}.
\tag{7.2}
$$

**Formality への依存。** まず affine homogeneous Poisson bracket $B_C$ に Kontsevich の formality を適用する。重み 0 なので各補正項が内部次数を保つ。twisted formality map が Poisson 中心を同じ star product の中心へ送ることを使い、$Q_0,Q_1$ を同時に持ち上げる。二つの像は同じ積に関する中心元だから相互にも可換である。この外部入力の版・仮定の独立確認は量子化研究の課題として扱う。

**正則列と平坦性。** $\Omega_{0,\hbar}a=0$ なら最初の非零 $\hbar$ 係数で $Q_0a_0=0$ となり矛盾。さらに $\hbar a=\Omega_{0,\hbar}b$ なら、還元して $Q_0b_0=0$、従って $b=\hbar b_1$、$a=\Omega_{0,\hbar}b_1$。よって一段目の商は $\hbar$-torsion-free。その各次数は有限生成の離散付値環上の torsion-free module なので自由である。可換極限で $Q_1$ は $S/(Q_0)$ の非零因子なので同じ議論をもう一度適用できる。これで二つの中心元の正則性、商の平坦性、Hilbert series を得る。

関係式の一次部分は

$$
[x_i,x_j]=\hbar\sum_{a<b}\Delta_{ab}c_{ijab}x_ax_b+O(\hbar^2).
$$

高次項と中心元の補正は選んだ積に依存する。可換式 $Q_a$ 自体が補正なしに中心的であるとは限らない。

任意の $(a,b)\ne(0,0)$ に対し $a\Omega_{0,\hbar}+b\Omega_{1,\hbar}$ は中心的非零因子で、商は対応する二次超曲面の平坦な量子化となる。従って中心的 quadric pencil は残るが、標準 ambient 内の $B_\hbar$ はあくまで二本の式による完全交叉である。量子化の一意性、全非可換変形の網羅性、任意の非零複素数での $\hbar$ の特殊化は導かれない。

### 形式的 ambient の AS 正則性：保持する証明と留保

資料は次の一般命題を証明している。連結次数付き $R$ 代数 $A_\hbar$ の各次数が有限自由で、還元が $N$ 個の次数 1 変数の多項式環なら、$K=\mathbb C((\hbar))$ 上の $A_K$ は quadratic Koszul AS 正則、大域次元と Gorenstein parameter は $N$、Hilbert series は $(1-t)^{-N}$。

論証は次の通りである。次数ごとの Nakayama により次数 1 で生成される。$L=A_{\hbar,1}$、$I_2=\ker(L\otimes L\to A_{\hbar,2})$ は有限自由。$T_R(L)/(I_2)\to A_\hbar$ の各次数の全射は、標的が自由なので $R$ 加群として分裂する。還元は多項式環の二次表示で同型なので、その核は Nakayama により零となる。

内部次数 $m$ の reduced bar complex は有限個の有限自由 $R$ 加群からなる。還元ホモロジーはホモロジー次数 $m$ にのみ現れ rank $\binom Nm$（$m>N$ なら零）。微分の単元成分を消去して可縮因子を除くと、残る最小複体の還元は微分零だから、その項はこの一つの次数にしか残らない。よって元のホモロジーも同じ rank の自由加群となり、相対 Koszul 性を得る。

二次双対の各次数の rank は $\binom Ni$、$i>N$ では零、還元は外積代数。最上次数を $R$ と同一視した積 pairing は還元で完全なので、行列式が単元となり持ち上げ後も完全。従って双対は Frobenius。$K$ 上の Koszul complex は長さ $N$ で、Frobenius 双対性から
$\operatorname{Ext}_{A_K}^i(K,A_K)=0$（$i\ne N$）、$\operatorname{Ext}_{A_K}^N(K,A_K)=K(N)$ を得る。最後に connected graded algebra の大域次元と自明加群の射影次元の関係を用いる。資料の参照は Artin–Tate–Van den Bergh, §2, p.41 であり、この最後の一般入力の全仮定の独立確認は残る。

この命題に **一般の $A_K$ の noetherian 性は含めない**。有限段階 $B_\hbar/\hbar^rB_\hbar$ は有限 $\hbar$-進 filtration の随伴次数環が可換 noetherian 環の有限拡大なので左右 noetherian であり、形式的な非可換 projective geometry は整合的な族 $\operatorname{qgr}(B_\hbar/\hbar^rB_\hbar)$ として扱える。右加群を用い、torsion は内部次数に関するものとする。

## 8. 曲面の affine chart と Rees 表示

$n=2$ で $s\ne0$ を選び、残る四つの線型座標を $u_0,u_1,u_2,u_3$ とする。$s=1$ 上で

$$
X\setminus D_s=\{\phi_0=\phi_1=0\}\subset\mathbb A^4,
\qquad \phi_a(u)=Q_a(1,u).
$$

各 $\phi_a$ は次数高々 2。括弧は定数倍を除き

$$
\{f,g\}=\det\frac{\partial(\phi_0,\phi_1,f,g)}
{\partial(u_0,u_1,u_2,u_3)}.
\tag{8.1}
$$

四変数・二つの Casimir である。(4.2) の括弧に $\partial_s$ 成分がないため、Kontsevich 積では $s$ は補正なしに中心的に保たれる。$A_\hbar/(s-1)$、$B_\hbar/(s-1)$ の $u$ の次数 filtration から Rees 代数を取ると、それぞれ元の斉次代数を回収する。これは中心的で正則な $s$ を用いる斉次化・非斉次化を各有限 $\hbar$-進段階で行うことで確認する。

$D_s$ が滑らかなら $s=0$ の境界の座標環は四変数の $(2,2)$ 完全交叉で、その斉次 Jacobian 括弧は classical Sklyanin bracket となる。ただし、任意の star product が次節の特定の表示になるとは主張しない。

## 9. 中心元まで指定した Sklyanin 模型

この節は $Q_a$ に $su_i$ という混合項がない特別な模型を扱う。一般の標識付き対 $(X,s)$ の全量子化を尽くす主張ではない。

$a,b\in\mathbb C$ を $ab(a+b)\ne0$ とし、

$$
c(\hbar)=-\frac{a+b}{1+\hbar^4ab},\qquad
a_1=a,\quad a_2=b,\quad a_3=c(\hbar).
\tag{9.1}
$$

次数 1 の生成元 $u_0,u_1,u_2,u_3$ を持つ $R$ 代数 $T_\hbar$ を

$$
[u_0,u_i]=\hbar a_i(u_ju_k+u_ku_j),\qquad
[u_j,u_k]=\hbar(u_0u_i+u_iu_0),
\tag{9.2}
$$

$(i,j,k)=(1,2,3),(2,3,1),(3,1,2)$ で定める。パラメータは

$$
a+b+c(\hbar)+\hbar^4abc(\hbar)=0
$$

を満たす。$K$ 上で $x_0=\hbar u_0$、$x_i=u_i$ と変換すると、通常の四次元 Sklyanin 代数 $S(\alpha,\beta,\gamma)$ に移り、

$$
(\alpha,\beta,\gamma)=(\hbar^2a,\hbar^2b,\hbar^2c(\hbar)),
\qquad\alpha+\beta+\gamma+\alpha\beta\gamma=0.
\tag{9.3}
$$

$\alpha,\beta,\gamma\notin\{0,\pm1\}$。資料は Smith–Stafford の (1.9.1), Theorems 5.4–5.5 を適用し、$T_K$ が noetherian、四次元 Koszul AS 正則、Hilbert series $(1-t)^{-4}$ であるとする。$T_\hbar/\hbar T_\hbar$ は可換多項式環で、各次数の $K$-rank と還元次元が等しいので、離散付値環上の構造定理により各次数は有限自由となる。

半古典括弧と二つの二次 Casimir は

$$
\{u_0,u_i\}=2a_i(0)u_ju_k,\qquad
\{u_j,u_k\}=2u_0u_i,
$$

$$
q_0=u_1^2+u_2^2+u_3^2,
\qquad q_1=u_0^2+(a+b)u_2^2+bu_3^2.
\tag{9.4}
$$

括弧の全体係数は
$-\tfrac12\det\partial(q_0,q_1,f,g)/\partial(u_0,u_1,u_2,u_3)$ である。

### 明示的な二つの中心元

$$
g_0=-\hbar^2u_0^2+u_1^2+u_2^2+u_3^2,
\qquad
g_1=u_0^2+\frac{a+b}{1-\hbar^2b}u_2^2
-\frac{a+c(\hbar)}{1+\hbar^2c(\hbar)}u_3^2.
\tag{9.5}
$$

資料が Smith–Stafford, Corollary 3.9 から用いる中心元は

$$
\Omega_1=-x_0^2+x_1^2+x_2^2+x_3^2,\qquad
\Omega_2=x_1^2+\frac{1+\alpha}{1-\beta}x_2^2
+\frac{1-\alpha}{1+\gamma}x_3^2.
$$

変数変換 (9.3) 後に $g_0=\Omega_1$、$g_1=(\Omega_2-\Omega_1)/\hbar^2$ とすれば (9.5) を得る。分母はすべて $R$ の単元なので $g_a\in T_\hbar$。torsion-free により $T_\hbar\hookrightarrow T_K$ なので $K$ 上の中心性から $R$ 上の中心性が従う。$c(0)=-(a+b)$ を代入すれば $g_a\bmod\hbar=q_a$ となる。特に $g_1$ の最後の係数の符号と $\hbar^4$ を含む (9.1) はこの表示の一部であり、省略しない。

### 五生成元の次数 4 曲面

$$
\rho_0\ne0,\qquad\rho_1/\rho_0\notin\{0,b,a+b\}
\tag{9.6}
$$

とし、中心的次数 1 変数 $s$ を加える。

$$
A_\hbar^{\rm sk}=T_\hbar[s],\qquad
B_\hbar^{\rm sk}=
\frac{T_\hbar[s]}{(g_0+\rho_0s^2,\ g_1+\rho_1s^2)}.
\tag{9.7}
$$

可換極限は

$$
X=\{q_0+\rho_0s^2=q_1+\rho_1s^2=0\}\subset\mathbb P^4.
$$

pencil の五つの特異パラメータは
$\infty,0,-b,-(a+b),-\rho_1/\rho_0$ で、仮定により相異なる。従って $X$ は滑らかな次数 4 の del Pezzo 曲面。(7.1) と同じ正則列の議論により (9.7) は平坦な量子化で、

$$
H_{A_\hbar^{\rm sk}}(t)=(1-t)^{-5},\qquad
H_{B_\hbar^{\rm sk}}(t)=\frac{(1-t^2)^2}{(1-t)^5}
=\frac{(1+t)^2}{(1-t)^3}.
$$

$K$ 上の ambient は中央多項式拡大として五次元 AS 正則かつ noetherian。境界と affine 補集合はそれぞれ

$$
B_\hbar^{\rm sk}/(s)=T_\hbar/(g_0,g_1),\qquad
B_\hbar^{\rm sk}/(s-1)=T_\hbar/(g_0+\rho_0,g_1+\rho_1).
$$

前者は $K$ 上で楕円曲線の twisted homogeneous coordinate ring になる。ただし楕円曲線と shift は量子化パラメータに依存し、可換極限の曲線と同一視して固定してはいない。

### 非形式的特殊化の範囲

この特殊模型の係数は $\hbar$ の有理関数である。分母が非零で、特殊化した $\alpha,\beta,\gamma\notin\{0,\pm1\}$ となる非零複素数 $\hbar=t$ には特殊化できる。$ab(a+b)\ne0$ の下では十分小さい $t\ne0$ がこれを満たす。

資料は Smith–Stafford, Theorem 5.4 の中心的正則列の可逆な線型変換として $g_0,g_1$ の正則性を用いる。この不変性は、$T_t/(\Omega_1,\Omega_2)$ の斉次基底の持ち上げが $\mathbb C[\Omega_1,\Omega_2]$ 上の自由基底になることからも分かる。生成性は次数帰納法、独立性は正則列の Hilbert series による。従って $T_t[s]$ は $\mathbb C[g_0,g_1,s]$ 上自由であり、$(g_0+\rho_0s^2,g_1+\rho_1s^2)$ も正則列である。

一般の $s$ では $Q_a(s,u)$ に $su_i$ が現れるため、単なる $T_\hbar[s]$ だけで全 Poisson 構造の量子化を記述したことにはならない。一般の $s$ については形式的存在とこの特殊な非形式的表示を区別する。

## 10. 混同しやすい三つの商

| 商 | 幾何学的役割 |
|---|---|
| $T/(g_0,g_1)$ | 楕円曲線の座標環。曲面ではない |
| $T/(ag_0+bg_1)$ | 非可換 quadric 曲面。滑らかな可換極限は $\mathbb P^1\times\mathbb P^1$ で del Pezzo 次数 8 |
| $T[s]/(g_0+\rho_0s^2,g_1+\rho_1s^2)$ | 五つの次数 1 生成元による次数 4 の del Pezzo 曲面の非可換完全交叉 |

第一の商の Hilbert series は $(1-t^2)^2/(1-t)^4$ で極の位数は 2、次数 4 の del Pezzo 曲面の座標環では極の位数は 3。可換 quadric 曲面の Segre 超平面類を $L$ とすれば $-K=2L$、$L^2=2$ なので $(-K)^2=8$ である。Sklyanin 代数の「次元 4」と del Pezzo の「次数 4」は異なる数値である。

## 11. 引用入力と次の確認点

以下は出発資料に記載された書誌と使用箇所。一次資料を今回全件再確認したという意味ではない。

- A. Kuznetsov and Y. Prokhorov, *On higher-dimensional del Pezzo varieties*, Izvestiya: Mathematics 87 (2023), 488–561, [arXiv:2206.01549](https://arxiv.org/abs/2206.01549), Theorem 1.2(iv)：次数 4 の標準モデル。
- I. Cheltsov and Y. Prokhorov, *Del Pezzo surfaces with infinite automorphism groups*, Algebraic Geometry 8 (2021), 319–357, [doi:10.14231/AG-2021-008](https://doi.org/10.14231/AG-2021-008), Theorem 2.5(ii),(iv)：曲面の反標準モデル。
- R. Donagi, *Group law on the intersection of two quadrics*, Annali della Scuola Normale Superiore di Pisa, Classe di Scienze (4) 7 (1980), no.2, 217–239, [一次資料 PDF](https://www.numdam.org/item/ASNSP_1980_4_7_2_217_0.pdf), §1.2, pp.221–222：同時対角化と判別式。
- F. Loray, J. V. Pereira and F. Touzet, *Foliations with trivial canonical bundle on Fano 3-folds*, [arXiv:1112.3871v3](https://arxiv.org/abs/1112.3871v3), Theorems 7.1, 9.1、§7 の表：三次元の分類。公刊版との照合は本リポジトリの文献調査記録を参照する。
- M. Kontsevich, *Deformation quantization of Poisson manifolds, I*, [arXiv:q-alg/9709040v1](https://arxiv.org/abs/q-alg/9709040v1), §§4.6.2,6,8：affine formality と中心。
- M. Artin, J. Tate and M. Van den Bergh, *Some algebras associated to automorphisms of elliptic curves*, The Grothendieck Festschrift, Vol.I, Progress in Mathematics 86, Birkhäuser, 1990, 33–85, §2,p.41：大域次元に関する入力。
- S. P. Smith and J. T. Stafford, *Regularity of the four dimensional Sklyanin algebra*, Compositio Mathematica 83 (1992), no.3, 259–289, [一次資料 PDF](https://www.numdam.org/article/CM_1992__83_3_259_0.pdf)：関係式 (0.2.1)–(0.2.2)、仮定 (1.9.1)、中心元 Corollary 3.9、正則列 Theorem 5.4、正則性・noetherian 性 Theorem 5.5。
- B. Pym, *Quantum deformations of projective three-space*, [arXiv:1403.6444v1](https://arxiv.org/abs/1403.6444v1), §3.3：$R(2,2)$ 型と classical Sklyanin bracket。現行の書誌・版の比較を別途要する。

Smith–Stafford の Theorem 5.4 は (1.9.1) または (1.9.4) の場合の定理であり、Theorem 5.5 は標数 2 でない任意の体について、除外される三つのパラメータ族を明示している。$K=\mathbb C((\hbar))$ が代数閉体でないことのみを理由に後者の適用を止める必要はない。中心的正則列については、必要なら代数閉包への忠実平坦基底拡大と降下を明記して用いる。

優先する未確認点は、大域同型と Jacobiator 持ち上げの独立再検証、intrinsic Jacobi scheme と座標 ideal の比較、三次元分類の一次資料の仮定、formality と中心の graded 版、Sklyanin 一次資料の仮定である。$n\ge4$ の全既約成分、全量子化の同型類、一般構造の非形式的有限表示はこのノートの完成した結論ではない。
