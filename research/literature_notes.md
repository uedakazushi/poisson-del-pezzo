# 先行研究と主張の位置づけ

2026-11-20（JST）・v1.2。次数 1・2 の滑らかな複素 del Pezzo 多様体に関する現行の文献確認メモ。
書誌情報は [references.bib](../references.bib) に収録する。以下の「確認」は指定した版の定義・定理文・該当する議論を読んだことを指し、引用論文の証明全体を独立に検証したことを意味しない。

## 現時点での結論

本研究では、$n\geq 2$、$-K_X=(n-1)H$、$H^n\in\{1,2\}$ を満たす滑らかな複素射影多様体 $X$ を扱う。固定した $X$ に対する分類、ambient lift、Jacobi 零スキームの同定、相対化とモジュライの構成を区別する。証明とその仮定は [現行原稿](../poisson-del-pezzo.tex) を参照する。

| 範囲 | 既存文献との関係 | 本研究での扱い |
| --- | --- | --- |
| $n=2$ | $\wedge^3T_X=0$ のため全 bivector が Poisson。反標準線型系の標準的記述で分類できる | 新規の分類として掲げない |
| $n=3$、次数 1・2 | Loray–Pereira–Touzet の分類で既知。射影化された空間の唯一の成分は $\operatorname{Rat}(1,1)$、次元は順に 2、4 | 既知結果との一致を明記する |
| $n\geq4$、次数 1・2 | 同一の一般性で全 Poisson 構造を分類する一次資料を、今回の調査では特定していない | 新規性は未確定。未発見を未公表の証拠としない |
| 曲面の同時無限小変形 | Hong–Xu Theorem 3.9 で次数1・2の $\dim H^2_\pi=10,9$ と $H^1_\pi=0$ が既知 | 大域的商スタックと比較し、次元自体を新発見としない |
| 族・モジュライ | 一般的な基底変換・商スタックの存在は既知。今回と同じ任意次元の相対分類の優先権は未確定 | twist と非被約基底を含む証明を本文に置く |
| Jacobi 零スキーム | 既約成分や被約多様体の分類と、Jacobi イデアルそのものの同定は別の主張 | イデアル一致の証明を原稿に置き、新規性は別途調査する |

次数 1 の $\mathbb A^n$、次数 2 の $\operatorname{Gr}(2,n+1)$ の Plücker 埋め込みのアフィン錐という記述は、原稿内の結果として提示する。低次元での既知性と、高次元・スキーム・持ち上げの各主張の新規性を一括して扱わない。

## 三次元の既知分類：LPT2013

F. Loray, J. V. Pereira, F. Touzet, *Foliations with trivial canonical bundle on Fano 3-folds*, Math. Nachr. **286** (2013), 921–940。DOI: [10.1002/mana.201100354](https://doi.org/10.1002/mana.201100354)。確認本文は [arXiv:1112.3871v3](https://arxiv.org/pdf/1112.3871v3)。

Theorem 7.1 と §7 の表は $\operatorname{Pic}(X)=\mathbb ZH$ の index 2 Fano 三次元多様体を扱い、次数 1・2 では $\operatorname{Rat}(1,1)$ の唯一の成分を与える。§9 の Theorem 9.1 は Poisson 構造の既約成分を分類する。この論文の $\operatorname{Poisson}(X)$ は $\mathbb P H^0(X,\wedge^2T_X)$ の中の空間なので、アフィンな Jacobi 零スキームとの比較ではスカラーと原点を区別する。

arXiv v3 は Theorem 9.1 の訂正を含むため、引用する定理文はこの版に固定する。この文献から任意次元の分類や Jacobi イデアルの一致を引用しない。

## スキーム構造の比較：Mayanskiy2015

E. Mayanskiy, *Poisson cohomology of two Fano threefolds*, J. Algebra **424** (2015), 21–45。DOI: [10.1016/j.jalgebra.2014.08.049](https://doi.org/10.1016/j.jalgebra.2014.08.049)。確認本文は [arXiv:1303.5916v1](https://arxiv.org/pdf/1303.5916v1)、Introduction pp. 2–3。

Theorem 1 は滑らかな cubic threefold の射影 Poisson 空間を Plücker 埋め込みされた $\operatorname{Gr}(2,5)$ と記述する。Theorem 3 は次数 5 の三次元多様体を扱う。p. 3 の Remark は、LPT の議論だけでは Poisson 空間のスキーム構造について情報が得られないことを指摘する。

この指摘により、既知の三次元の成分分類と、今回の次数 1・2 に関する Jacobi イデアルの同定を区別する必要が明確になる。ただし Mayanskiy の対象は次数 3 と 5 であり、次数 1・2 のスキーム同定を証明する文献ではない。また、この比較だけから今回のスキームに関する結果の新規性が確定するわけではない。

## 「del Pezzo foliation」との区別：AD2013

C. Araujo, S. Druel, *On Fano foliations*, Adv. Math. **238** (2013), 70–118。確認本文は [arXiv:1112.4512v2](https://arxiv.org/pdf/1112.4512v2)、Definitions 2.8, 2.11 および Theorem 1.1。

この文献の del Pezzo foliation は、foliation 自身の反標準類 $-K_{\mathcal F}$ が ample で、foliation の index が $\operatorname{rank}(\mathcal F)-1$ となるものである。周囲の多様体 $X$ が del Pezzo であることだけでは、この条件は従わない。Poisson 構造が定める葉層へ適用する際には $K_{\mathcal F}$ と正値性を別に確認する必要があり、名称の一致から直接の分類定理として扱わない。

## 重み付き模型の引用範囲

**KP2023**：A. Kuznetsov, Y. Prokhorov, *On higher-dimensional del Pezzo varieties*, Izv. Math. **87** (2023), 488–561。DOI: [10.4213/im9385e](https://doi.org/10.4213/im9385e)。[arXiv:2206.01549v2](https://arxiv.org/pdf/2206.01549v2) の Theorem 1.2(i),(ii) は、$n\geq3$ の次数 1・2 の模型をそれぞれ $X_6\subset\mathbb P(1^n,2,3)$、$X_4\subset\mathbb P(1^{n+1},2)$ として記述する。Proposition 2.2(i) は $\dim|H|=d+n-2$ を与える。この定理を $n=2$ にそのまま適用しない。

**CP2021**：I. Cheltsov, Y. Prokhorov, *Del Pezzo surfaces with infinite automorphism groups*, Algebr. Geom. **8** (2021), 319–357。DOI: [10.14231/AG-2021-008](https://doi.org/10.14231/AG-2021-008)。[出版本文](https://content.algebraicgeometry.nl/2021-3/2021-3-008.pdf) の Theorem 2.5(v) は次数 2 の二重平面・重み付き quartic、(vi),(vii) は次数 1 の反標準 pencil・基点・重み付き sextic を扱う。この標準模型の定理には無限自己同型群を仮定せず、滑らかな曲面にも適用できる。

## Fujita のレビューと定義

**Fujita1980**：*On the structure of polarized manifolds with total deficiency one, I*, J. Math. Soc. Japan **32** (1980), 709–725。[出版本文](https://www.jstage.jst.go.jp/article/jmath1948/32/4/32_4_709/_pdf) の Theorem (1.9), Definition (1.13) は $-K=(n-1)H$ と偏極付き del Pezzo の定義を比較する。原始的な $H$ を定義に要求しないため、$(\mathbb P^3,\mathcal O(2))$ も含まれる。Lemma (1.10)、Theorems (2.1), (2.2), (2.5)、§3 をレビューの典拠とした。

**Fujita1984**：同 III, J. Math. Soc. Japan **36** (1984), 75–89。[出版本文](https://www.jstage.jst.go.jp/article/jmath1948/36/1/36_1_75/_pdf/-char/en) の Theorem (13.6) は次数1の唯一の単純基点と種数1の曲線の族（曲面では pencil）、Theorems (14.6), (16.7) は重み付き六次模型の典拠である。§16 の $g=1$ への適用は (16.3) に明記されている。

高次元の模型一覧には KP2023 Theorem 1.2 全体を用いた。Picard 数1を一律に仮定しない。基本偏極のクラスの一意性と、族上での実際の線束・反標準同型の選択は別問題である。

## 曲面の Poisson cohomology：Hong–Xu

W. Hong, P. Xu, *Poisson cohomology of del Pezzo surfaces*, [arXiv:1001.1082v2](https://arxiv.org/abs/1001.1082v2)。[本文](https://arxiv.org/pdf/1001.1082) の Theorem 3.9、p.10、式(34) は、$\mathbb P^2$ の一般位置の $r=5,\ldots,8$ 点の blow-up $B_r$ に対し

$$
H^0_\pi=\mathbb C,\quad H^1_\pi=0,\quad
\dim H^2_\pi=r+2,\quad H^i_\pi=0\ (i>2)
$$

を与える。次数1・2では $r=8,7$ なので変形次元10・9が既知であり、今回の滑らかなモジュライスタックの次元に一致する。曲面の任意の bivector が Poisson であることも既知である。今回の結果の位置付けは、この数値ではなく任意次元の相対 Jacobi スキームと同変な商構成に置く。

書誌年は arXiv v2 の日付2011を用いた。PDF内部の日付と異なるが、未確認の雑誌掲載情報は補っていない。

## 族とスタックの外部入力

Stacks Project の以下の一次資料を確認した。

- [Tag 0B91](https://stacks.math.columbia.edu/tag/0B91), Lemma 36.30.4：proper finite-presentation flat morphism と perfect complex の導来 pushforward の perfect 性、任意の導来基底変換。本稿では普遍切断の分裂をさらに示して通常の $p_*\wedge^2T$ の基底変換を得る。
- [Tag 06FI](https://stacks.math.columbia.edu/tag/06FI), Theorem 97.17.2：flat locally-finite-presentation groupoid の商の代数性。
- [Tag 06N3](https://stacks.math.columbia.edu/tag/06N3), Theorem 101.21.6 と [Tag 0DSL](https://stacks.math.columbia.edu/tag/0DSL), Lemma 101.22.2：DM 性と unramified な幾何学的 stabilizer の判定。本稿では有限自己同型を重みと Koszul 完全性から独立に示す。

- [Tag 0D2C](https://stacks.math.columbia.edu/tag/0D2C), Proposition 99.11.8、[Tag 0DNI](https://stacks.math.columbia.edu/tag/0DNI), Lemma 108.9.3、[Tag 0DME](https://stacks.math.columbia.edu/tag/0DME), Lemma 108.9.1：相対 Picard 層の代数空間性・局所有限表示性・線束の fppf 局所表示。[Tag 0D28](https://stacks.math.columbia.edu/tag/0D28), Lemma 99.11.4 は切断を持つ族で Picard 類を線束で表すことを保証し、平方零拡大上での étale 局所的な持ち上げに用いる。基本偏極類の一意な相対化には、さらに $H^1(\mathcal O)=H^2(\mathcal O)=0$ と torsion-free Picard 群の本文証明を用いる。

これらの一般定理自体を本研究の成果として扱わない。相対法線・Euler 列、正規形の相対切断環、座標変換の character、およびその Poisson 方程式への作用が、本稿で具体的に証明する部分である。

## 公表前に残る文献上の課題

- $n\geq4$ の全 Poisson 分類、重み付き周囲空間への持ち上げ、Jacobi 零スキームの各主張について、引用文献の参照先および高余次元 foliation の文献を追加調査する。
- 既知の対象の別証明、明示公式、スキームに関する強化、高次元への拡張を分け、Introduction で具体的に比較する。
- 量子化については **EG2010** の Lemma 7.4.2、Proposition 8.1.1(i) と、その証明中の相対的議論の範囲を保つ。任意のパラメータ環への拡張は原稿内の議論を必要とし、generic な中心・Hochschild cohomology に関する結論を無条件には引用しない。
- 本文を未確認の参考文献を主要定理の依存先にしない。特に **ATV1990** の §2 p. 41、**Cassidy1999**、**Cassidy2003** の詳細な仮定は今回の調査では未確認であり、書誌にその状態を記載している。

現段階の原稿は、以上の確認範囲で数学的主張と証明を整理する研究稿である。公表用の新規性確認を完了したものとは扱わない。

## Plücker 錐の標準性と特異点（v1.2 の使用箇所）

- Svanes, *Arithmetic Normality for Projective Embeddings of Flag Manifolds*, Math. Scand. **33** (1973), 55–68, https://www.mscand.dk/article/download/11471/9488. Grassmann の Plücker 埋め込みの射影正規性に関する一次資料と，ACM 性についての既知結果の文献案内。
- De Concini–Procesi, *Hodge algebras: a survey*, Astérisque **87–88** (1981), 79–83, https://www.numdam.org/item/AST_1981__87-88__79_0/. 標準単項式基底、Grassmann の arithmetically Cohen–Macaulay 性（解説・引用先）を確認。
- Kollár–Mori, *Birational Geometry of Algebraic Varieties*, CUP (1998), DOI:10.1017/CBO9780511662560, Chapter 5. terminal/klt/rational の一般理論。
- 頂点 blow-up が tautological line の全空間である事実、canonical line と discrepancy の計算は現行論文 `lemma:cone-blowup`・`prop:plucker-terminal` で示す。これらの一般的代数幾何の既知結果を本研究の新規成果とは主張しない。降下の優先権は未確認。
