# 研究ノート：次数1・2と del Pezzo Poisson 構造

2026-11-20（JST） / v1.0

このノートは現行の数学的知識と次の着手方法をまとめる。完全な証明は [論文](../papers/dp12_poisson.tex) に置き、ここでは依存関係と論文外の課題を補う。[研究方針](../00_research_plan.md) を先に読む。

## 1. 記法と現在の証明の構造

基礎体は $\mathbb C$。$X$ は滑らかな連結射影 $n$ 次元多様体、$n\geq2$、$H$ は ample Cartier、$-K_X=(n-1)H$。

| 次数 | 多項式環・重み | 定義式 | 定数テンソル |
| --- | --- | --- | --- |
| 1 | $S=\mathbb C[x_0,\dots,x_{n-1},y,z]$、重み $(1^n,2,3)$ | $F=z^2-y^3-A_4(x)y-A_6(x)$ | $C=D\wedge\partial_y\wedge\partial_z$、$D$ は定数 $x$ ベクトル |
| 2 | $S=\mathbb C[x_0,\dots,x_n,z]$、重み $(1^{n+1},2)$ | $F=z^2-f_4(x)$ | $C=P\wedge\partial_z$、$P$ は定数 $x$ 二重ベクトル |

大域 bivector は $\widetilde\pi=\iota_{dF}C$ に一意に対応する。縮約は $\iota_\alpha(v\wedge w)=\alpha(v)w-\alpha(w)v$。$\{a,b\}=\widetilde\pi(da,db)$。

証明の依存は「標準模型 → weighted Euler 列の消滅 → Casimir 補正 → 偏微分 Koszul 複体 → Jacobi 公式 → スキーム論的な係数回収」である。
特に次数2の記法は

$$
P=\sum_{i<j}a_{ij}\partial_i\wedge\partial_j,\quad
V_i=\sum_j a_{ij}f_j,\quad
\widetilde\pi=2zP+\sum_iV_i\partial_i\wedge\partial_z,
$$

$$
J_{ijk}=2\sum_lq_{ijkl}f_l,\qquad
q_{ijkl}=a_{ij}a_{kl}-a_{ik}a_{jl}+a_{il}a_{jk}.
$$

$J(x_i,x_j,z)=0$。$E\wedge J$ の $z$ 成分から $2zJ_{ijk}$ を取り、
$R_5=\mathbb C[x]_5\oplus z\mathbb C[x]_3$ の第二成分へ射影して、偏微分 $f_l$ の線型独立性を使う。
これにより各 $q_{ijkl}$ は **射影的 Jacobi 二次写像の係数の線型結合**になる。この線型回収が、根基の一致を超えてイデアルそのものを同定する核心である。

任意次元の証明は `thm:jacobi-scheme`。検算コードは有限個の次元で公式の符号と係数回収を確認するものであり、この大域証明を代替しない。

## 2. 変形・compatibility・原点

次数1の全ての括弧は相互に compatible。次数2では Poisson パラメータ $P,Q$ が compatible である必要十分条件は $P\wedge Q=0$。非零なら対応する二平面の交わりが非零であることと同値である。

次数2の Poisson cone は次元 $2n-1$、非零部は滑らか、原点の接空間は次元 $\binom{n+1}{2}$。$n\geq3$ で原点のみ特異。零点からの一次変形 $\varepsilon Q$ は常に許されるが、二次へ持ち上がるには $Q\wedge Q=0$ が必要十分。証明と階数4の一次方向の反例は論文 `sec:infinitesimal`。

これは **固定した多様体上の bivector の変形**についての主張である。$H^1(T_X)$ を含む多様体自体の変形、Poisson cohomology 全体、gauge 商、非可換圏の変形の unobstructedness を結論しない。

## 3. 相対化への具体的な着手

### 座標付きの族

次数1では $(A_4,A_6)$、次数2では $f_4$ の係数 affine space から、対応する $X$ が滑らかな locus $U_d$ を取る。標準式の $z^2$ 係数を1に固定する。この正規化付きの族を先に扱い、後から座標変換の群作用を考える。

次数2で $f_j$ の三次単項式係数を並べた行列を $M(f)$ とする。各滑らかなファイバーで列階数は $n+1$ なので、非零な最大小行列式を可逆化した開集合が $U_2$ を覆う。その開集合で左逆 $L(f)$ を作れば、固定 $X$ の証明の線型汎関数 $\lambda_j$ を正則に選べる。

**未完成の課題：** 相対 Euler 列・cohomology and base change を明示して $p_*\wedge^2T_{\mathcal X/U_d}$ を同定し、Jacobi 零スキームの形成と非被約基底変換との両立を証明する。その後、$L(f)$ の選択によらないイデアル同定を貼り合わせる。点ごとの等式だけを証明としては使わない。

### 定義式の線束と同変性

同じ座標で $F$ を $cF$ に変えると、同じ bivector を表す定数テンソルは $c^{-1}C$ に変わる。従って定数テンソル空間を intrinsic な affine パラメータ空間とみなす際には、定義式のスカラーが作用する線束を含める必要がある。

さらに標準二重被覆の involution $\tau:(x,y,z)\mapsto(x,y,-z)$（次数2では $y$ を除く）を考える。$F$ は不変で、$x$ の一次切断も不変である。しかし pushforward は $\partial_z\mapsto-\partial_z$ なので

$$
\tau_*\bigl(\iota_{dF}C\bigr)
=\iota_{dF}(\tau_*C)=-\iota_{dF}C.
$$

従って $H^0(X,H)$ 上の作用から、bivector 空間上の作用をそのまま復元することはできない。射影化するとこの $-1$ は消えるので Grassmann 表示と矛盾しない。これは次の同変性計算の必須チェックである。本文の分類を使った直接の計算であり、この involution の観察の新規性は主張しない。

## 4. 形式量子化の保証範囲

外部入力は affine space 上の formality。$\tilde\pi$ の重み0から積の各項が内部次数を保存し、$F$ の twisted image が中心元 $\Omega_\hbar=F+O(\hbar)$ になる。各内部次数の有限自由性と、可換極限の $F$ の非零因子性により、中心商も有限自由になる。

活性な3変数以外の $s_i$ は正規化した graph formula で厳密に中心的。従って中心的線型関係による曲面切断を扱える。曲面では EG2010 の potential と Rees 構成を現行論文に保持した。

次の主張は未解決または追加仮定を要する。

- 全 Poisson パラメータ空間上の一つの量子化、その座標変換に関する降下。
- 形式級数の収束または代数化、任意の非零複素 $\hbar$ への特殊化。
- 全特殊化の AS 正則性。論文 `prop:central-as-extension` の noetherian 性、中心的非零因子、AS正則な商という仮定を満たすことを先に検証する。
- 中心元の高次補正の閉じた公式、量子化の一意性、全 `coh(X)` 変形の網羅性。

## 5. 次数3・4との関係

重み付き模型が次数1・2の自由度を強く制限する。次数3では通常の cubic hypersurface となり、定数テンソルの許される形が変わる。詳細は [nc-cubic の研究方針](https://github.com/uedakazushi/nc-cubic/blob/main/00_research_plan.md) を参照し、本稿の rank2結論を次数3の全構造へ一般化しない。

次数4では二つの quadratic Casimir による $\bigwedge^4V$ 表示を用いる。$n\geq5$ には階数4の構造があり、全てを Grassmann 型にすることはできない。比較に必要な式、非一意lift、曲面の明示模型は [dp4_comparison.md](dp4_comparison.md) に置く。既存 [poisson-22ci](https://github.com/uedakazushi/poisson-22ci) と [nc-22ci](https://github.com/uedakazushi/nc-22ci) の最新の一般構造・例外層の解析全体をここへ複製しない。

## 6. 文献・出発資料・検証

一次文献の確認箇所と未確認箇所は [literature_notes.md](literature_notes.md)、書誌は [references.bib](../references.bib)。

出発資料は「次数1・2・4の del Pezzo manifold 上の Poisson 構造と非可換幾何」、2026-11-11 v2.0、`del_Pezzo_1_2_4_Poisson_quantization_20261111_v2.pdf`（表紙を含む30頁）。次数1・2の §§1–9を読み、現行TeXへ再構成した。元TeXは今回特定できなかったため、取得済みのPDFから数式・証明を照合した。旧PDFの複製や変更履歴を現行ツリーに置かず、研究を再開するのに必要な内容は現行ソースへ移した。次数4は比較に必要な内容を別ノートに整理し、詳細分類の正本を関連repoに置く。

数学的な点検、厳密検算、組版はそれぞれ別の検証である。現在の実行結果と再現方法は [docs/reproduction.md](../docs/reproduction.md)。未解決問題や未確認の優先権を、生成・組版の成功によって解決済みとはしない。
