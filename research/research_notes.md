# 研究ノート：次数1・2と del Pezzo Poisson 構造

2026-11-20（JST） / v1.4

このノートは現行の数学的知識と次の着手方法をまとめる。完全な証明は [論文](../papers/poisson-del-pezzo.tex) に置き、ここでは依存関係と論文外の課題を補う。[研究方針](../00_research_plan.md) を先に読む。

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

相対分類により、零 Poisson 構造での **多様体と bivector の同時変形**にも同じ二次障害が残る。座標付きの一次方向を $(\dot f,Q)$ とすると、二次へ延長できる必要十分条件は $Q\wedge Q=0$ であり、$\dot f$ では相殺できない。条件が成立すれば $(f+t\dot f,tQ)$ で全形式次数へ延長できる。これは `cor:relative-deformations` で証明した。Poisson cohomology 全体や非可換圏の変形の unobstructedness を結論するものではない。

## 3. 族とモジュライの構成

### 相対化の証明の要点

次数1では $(A_4,A_6)$、次数2では $f_4$ の係数 affine space から滑らかな locus $U_d$ を取る。普遍 Casimir 公式は各幾何学的ファイバーの bivector の基底を与える。proper perfect base change で得られる有限自由複体の次数0にこの基底を直和因子として取り、残りの微分の最大小行列式を可逆化する。これが任意基底変換の証明であり、ファイバーの次元が一定というだけの議論で代用しない。

次数2では偏微分 $f_j$ の三次単項式係数行列 $M(f)$ の列階数が $n+1$ である。最大小行列式を可逆化して左逆を作ると、$E\wedge J$ の $z$ 成分から Plücker 二次式を係数線型結合として回収できる。これにより相対 Jacobi イデアルが厳密に一致する。$p_*\wedge^3T$ の局所自由性は不要である。完全証明は `sec:families`。

### 同変性と線束

残余群と作用は次の通り。

- 次数1：$\widetilde G_1=\mathrm{GL}_n\times\mathbb G_m$、$(x,y,z)\mapsto(Ax,t^2y,t^3z)$。
  $(A_4,A_6,D)\mapsto(t^4A_4(A^{-1}x),t^6A_6(A^{-1}x),t^{-1}AD)$。
  $Z_1=\{(\lambda I,\lambda)\}$ を除いた $G_1\simeq\mathrm{GL}_n$ を使う。
- 次数2：$\widetilde G_2=\mathrm{GL}_{n+1}\times\mathbb G_m$、$(x,z)\mapsto(Ax,bz)$。
  $(f_4,P)\mapsto(b^2f_4(A^{-1}x),b^{-1}(\wedge^2A)P)$。
  $Z_2=\{(\lambda I,\lambda^2)\}$ を除いた $G_2$ を使う。

一般に $F'\circ\varphi=cF$ なら、Casimir テンソルは $C\mapsto c^{-1}\varphi_*C$ と変換する。$z\mapsto-z$ は方程式と $x$ の一次切断に自明に作用するが、bivector の符号を反転する。基本線束の一次切断の作用だけを見て affine パラメータを貼り合わせてはいけない。

実際の基本線束 $H$ を選べる族では

$$
\mathcal E=p_*H,\qquad
\mathcal L=p_*(\omega_{\mathcal X/T}^{-1}\otimes H^{-(n-1)}),\qquad
\mathcal V=p_*\wedge^2T_{\mathcal X/T}
\simeq\wedge^{n-1}\mathcal E\otimes\mathcal L.
$$

$H\mapsto H\otimes p^*M$ では $\mathcal E$ に $M$、$\mathcal L$ に $M^{-(n-1)}$ が掛かるので相殺する。$\mathcal V$ とその Poisson 錐は基本偏極のクラスだけを指定したスタックへ降下する。$\mathcal E$ や $H$ 自身の大域的な降下を仮定する必要はない。射影化も Grassmann 族として降下し、$\mathbb P(\mathcal V)$ 内の閉部分として射影的になる。

### 内在的モジュライと商表示

$$
\mathcal D_{n,d}=[U_d/G_d],\qquad
\mathcal P_{n,d}=[(U_d\times\mathfrak C_{d,n})/G_d],
$$

ここで $\mathfrak C_{1,n}=\mathbb A^n$、$\mathfrak C_{2,n}=\operatorname{Cone}\operatorname{Gr}(2,n+1)$。実際の線束とその同型を記憶するスタックには $\widetilde G_d$ を使う。この非 rigid なスタックには $\mathbb G_m$ の自己同型が残り、DM とは呼ばない。

$H^0(T_X)=0$ は、重み0の接ベクトル場を Euler 方向で補正し、偏微分の Koszul syzygy の係数次数 $w_i+w_j-m<0$ を使うことで証明する。有限 stabilizer と商表示から rigid 化したスタックは DM となる。忘却射は affine、有限表示、平坦。完全な定義と証明は `sec:moduli`。

基本偏極のクラスは、相対 Picard 層の étale 性と各ファイバーの Picard 群の torsion-free 性により、無標識の滑らかな del Pezzo 族にも一意に定まる。従って $\mathcal D_{n,d}$ は無標識の多様体のモジュライとも同値である。実際の基本線束を大域的に選べるとは限らない。証明は `lemma:fundamental-polarization-class`。

スタックへの幾何学的点 $[X]\to\mathcal D_{n,d}$ に沿うファイバーは $\operatorname{Pois}_{\mathrm{sch}}(X)$ 自身である。$X$ の同型類だけを固定して自己同型も残すスタック $[\operatorname{Pois}_{\mathrm{sch}}(X)/\operatorname{Aut}(X,[H])]$ とは異なる。二重被覆 involution は $\pi$ と $-\pi$ を同型にするが、非零 $\pi$ を固定しない。射影化後はこの差が消える。

次数2、$n\geq3$ で非滑らかな点の集合が零切断に等しいという結果は **スタック**についてである。$n=2$ では全体が滑らかである。特異部分スキームが被約であることや coarse space の特異点を同定したことを意味しない。有限stabilizerだけから一般のDMスタックの分離性を推測してはいけない。本稿では `lemma:affine-parameter-open` で係数空間のaffine性を示し、Lunaの定理によって有限対角と粗空間を得る。

### 全族を含む定義と成分数

`def:poisson-moduli-stack` の対象はsmooth proper finite-presentationな族と相対切断 $\pi$ であり、$[\pi,\pi]=0$ を切断の等式として課す。反標準束は各fiberでampleなので相対ampleとなる。代数空間としてfppf下降した後も、この束によりschemeとなる。任意基底上で一つの射影空間への大域閉埋込みを別途要求しない。

正規形のtorsorは、係数 $u\in U_d$ とその標準模型から所与の線束付き族への同型を組にした**正規化座標表示の層**である。固定二模型間のIsom層自体ではない。$G_d$-torsorが大域的に $\widetilde G_d$-torsorへ持ち上がるとは仮定せず、基本線束を大域的に持たない族も含める。

`thm:poisson-moduli-components` により、各 $n\ge2,d=1,2$ の $\mathcal P_{n,d}$ は幾何学的に整・正規・CMであり、**1成分**。非零部分と射影版も1成分である。零切断の余次元は $n$ または $2n-1$、非零部分のスキーム論的閉包は全体なので、零点の特異性は追加成分を意味しない。

`prop:poisson-degree-components` は、全体上に存在する反標準束のEuler標数の有限差分から $(-K)^n=(n-1)^n d$ の局所定数性を示す。従って固定 $n$ で次数1・2を許すstackは開閉分解され、**合計2成分**。基本線束の大域選択に依存しない。

非零族は全ての幾何学的基底点で $\pi_t\ne0$ となるものをいう。これは各 $X_t$ 上のどの点でも消えないという条件ではない。大域切断 $t\pi_0$ が非零でも $t=0$ で零になる。また双対数上の $\varepsilon\pi_0$ は全幾何fiberで零だが零切断には属さない。射影版は $p_*\wedge^2T$ の線部分束（局所直和因子）を指定する族であり、大域生成元を要求しない。詳しくは `rem:familywise-nonzero-poisson`。

成分数は構造定理と全族の商表示の帰結として確定した。残る課題はこの数値の再決定ではなく、先行結果との比較、各成分の一般点の幾何、相対量子化の下降である。

## 4. 粗忘却射、自己同型、解消

### 全滑らか領域の粗空間と平坦性

次数1の判別式開集合は、補助変数 $t$ を用いた $n+1$ 個の通常斉次式

$$t^2\partial_iA_4+\partial_iA_6\ (0\le i<n),\qquad 3t^4+A_4$$

のresultantの非消滅領域である。次数2は四次形式の通常の判別式を用いる。どちらもaffineなので、有限stabilizerを持つ還元群の作用についてのLuna I§4 p.90の定理を適用できる。これにより有限対角、分離性、affine粗空間を構成する。$A_d=\mathcal O(U_d)$、$R_{d,n}=\mathcal O(C_{d,n})$ として

$$M_{n,d}=\operatorname{Spec} A_d^{G_d},\qquad
N_{n,d}=\operatorname{Spec}(A_d\otimes R_{d,n})^{G_d}.$$

**平坦性の正確な判定**は `thm:coarse-flat-locus`：

$$\operatorname{Flat}(N_{n,d}\to M_{n,d})=f^{-1}(M_{n,d}^{\mathrm{sm}}).$$

証明の要点は、基底のLuna slice上で $(S\times C_{d,n})/H\to S/H$ とすること、有限群不変環のCohen–Macaulay性、ファイバーの定次元性、各固定 $X$ の一般非零Poisson構造が自己同型を消すことである。滑らかな基底上ではmiracle flatness、特異基底上では一般Poisson対の粗空間が正則であることと正則性の平坦降下を使う。平坦locusの開性により、特異基底の上ではファイバー内の全ての点が非平坦となる。一般の還元群による任意のCM環の不変環をCMと仮定する議論ではない。

粗ファイバーの**被約化**は常に $C_{d,n}/\operatorname{Aut}(X)$ で、ファイバーは位相的に既約、次元は次数1で $n$、次数2で $2n-1$。スキーム構造には基底sliceの有限Artin環の冪零部分が残り得る。

### 自己同型を消す構造と射影化

Poissonパラメータの表現は $G_1\simeq\mathrm{GL}_n$ では標準表現、$G_2$ では $b^{-1}\wedge^2A$ であり、どちらも忠実である。従って**任意の固定した $X$** に対して一般非零 $\pi$ は $\operatorname{Aut}(X,\pi)=1$ を満たす。全ての $X$ が一般的であることを仮定しない。

射影化の一般安定化群は、次数2で $\mu_2$。次数1では $A_4\ne0$ で $\mu_2$、$A_4=0$ で $\mu_6$。後者を単なるdeck対合と混同しない。一般多様体自体の自己同型群は両次数とも $\mu_2$ であり、その非空稠密開部分では粗基底が滑らかで、粗Poisson空間はétale局所的に $S\times C_{d,n}^{(2)}$ となる。

### 次数1の明示的な非平坦・非被約ファイバー

$X:z^2-y^3-f_6(x)=0$ で一般の $f_6$ を取ると、全 $n\ge2$ で $\operatorname{Aut}(X)=\mu_6$ とできる。$a=\binom{n+3}{4}$、$b=\binom{n+5}{6}-n^2$ とすれば、零Poisson構造での粗忘却射の完成局所環は

$$A=\mathbb C[[s_1,\ldots,s_b,u_1,\ldots,u_a]]^{\mu_3}
\longrightarrow B=\mathbb C[[s,u,v_1,\ldots,v_n]]^{\mu_6},$$

であり、点の座標の重みは $(s,u,v)\mapsto(s,\zeta^2u,\zeta v)$。$u$ は四次係数の変形、$s$ は六次係数の変形を軌道方向で割ったもの、$v$ はPoissonパラメータである。

$v$ 次数2の直和因子には、$u$ 次数 $2\pmod3$ の共変加群が現れる。この加群は階数1だが最小生成元を $\binom{a+1}{2}>1$ 個必要とするので非平坦。これは一般の平坦領域定理とは独立な局所計算にもなる。$(X,0)$ の像における粗ファイバーの完成局所環は

$$B/\mathfrak m_AB\simeq(\mathbb C[[u,v]]/(u)^3)^{\mu_6}.$$

$c=u_1v_1^4$ は $c^2\ne0$、$c^3=0$ を満たす。被約化 $\mathbb C[[v]]^{\mu_6}$ だけではこのファイバーを記述できない。非零 $\pi$ では自己同型が自明で全粗空間は滑らかだが、基底の粗空間は特異なので、そのファイバー内の全ての点で非平坦となる。完全証明は `thm:coarse-nonflat-degree-one` とその直後の系。

曲面での再現可能な具体例は

$$f_6=x_0x_1(x_0-x_1)(x_0-3x_1)(x_0-7x_1)(x_0-11x_1).$$

6個の根は相異なる。`computations/verify_coarse.py` は最初の3点の像を全て選ぶ120個の射影変換を有理数体上で列挙し、この6点を保つ変換が恒等元だけであることを厳密に確認する。これは明示的曲面の有限計算による証明書であり、任意次元の存在定理の代用ではない。ここでは $a=5,b=3$、上の階数1加群の最小生成元数は15。

### 対合商と解消の関係

被覆対合だけを除いた基底 $\mathcal B=[U_d/(G_d/\mu_2)]$ 上では、相対粗Poisson錐は偶数Veronese $C_{d,n}^{(2)}=\operatorname{Spec}R_{d,n}^{(2)}$ である。これは任意基底変換と可換で、相対粗忘却射は平坦。追加自己同型を除く全粗空間と区別する。もとの零切断への制限は $\mathcal D\to\mathcal B$ だが、粗側零切断のスキーム論的逆像は頂点イデアルの二乗で厚くなる。

$Y=\mathbb P^{n-1}$ または $\operatorname{Gr}(2,n+1)$ とする。もとの錐の零点blow-upは $\operatorname{Tot}\mathcal O_Y(-1)$、符号商では $\operatorname{Tot}\mathcal O_Y(-2)$。族では元のPoisson表現の線型化を保持して降下する。相対粗解消を $\overline{\mathcal R}$、例外因子を $\overline E$ とすると

$$\mathcal R\simeq\sqrt[2]{(\overline{\mathcal R},\overline E)},\qquad
r^*\overline E=2E.$$

この比較は追加自己同型の存在にかかわらず相対粗空間として成立する。全粗空間の解消と自動同一視しない。

### 符号商の特異点

$-K_Y=rH$ とすると、$r=n$（次数1）、$r=n+1$（次数2）。符号商の標準指数は $2/\gcd(2,r)$、頂点blow-upのdiscrepancyは $r/2-1$。次数1曲面は $A_1$、canonicalだが非terminal、それ以外はterminal。Gorensteinとなるのは次数1で $n$ 偶数、次数2で $n$ 奇数。$r$ 奇数のときもとの錐がindex-one coverとなる。

符号商は次数1曲面だけがhypersurfaceであり、その他は非lci。次数2で元の錐が滑らかである $n=2$ でも、符号商は指数2の三次元非lci特異点である。証明は `sec:singularities`。標準単項式・Veronese錐・標準指数の一般論は既知であり、Poissonモジュライへの同変な適用の新規性は未確認。

## 5. 形式量子化の保証範囲

外部入力は affine space 上の formality。$\tilde\pi$ の重み0から積の各項が内部次数を保存し、$F$ の twisted image が中心元 $\Omega_\hbar=F+O(\hbar)$ になる。各内部次数の有限自由性と、可換極限の $F$ の非零因子性により、中心商も有限自由になる。

活性な3変数以外の $s_i$ は正規化した graph formula で厳密に中心的。従って中心的線型関係による曲面切断を扱える。曲面では EG2010 の potential と Rees 構成を現行論文に保持した。

次の主張は未解決または追加仮定を要する。

- 全 Poisson パラメータ空間上の一つの量子化、その座標変換に関する降下。
- 形式級数の収束または代数化、任意の非零複素 $\hbar$ への特殊化。
- 全特殊化の AS 正則性。論文 `prop:central-as-extension` の noetherian 性、中心的非零因子、AS正則な商という仮定を満たすことを先に検証する。
- 中心元の高次補正の閉じた公式、量子化の一意性、全 `coh(X)` 変形の網羅性。

## 6. 次数3・4との関係

重み付き模型が次数1・2の自由度を強く制限する。次数3では通常の cubic hypersurface となり、定数テンソルの許される形が変わる。詳細は [nc-cubic の研究方針](https://github.com/uedakazushi/nc-cubic/blob/main/00_research_plan.md) を参照し、本稿の rank2結論を次数3の全構造へ一般化しない。

次数4では二つの quadratic Casimir による $\bigwedge^4V$ 表示を用いる。$n\geq5$ には階数4の構造があり、全てを Grassmann 型にすることはできない。比較に必要な式、非一意lift、曲面の明示模型は [dp4_comparison.md](dp4_comparison.md) に置く。既存 [poisson-22ci](https://github.com/uedakazushi/poisson-22ci) と [nc-22ci](https://github.com/uedakazushi/nc-22ci) の最新の一般構造・例外層の解析全体をここへ複製しない。

## 7. 文献・出発資料・検証

一次文献の確認箇所と未確認箇所は [literature_notes.md](literature_notes.md)、書誌は [references.bib](../references.bib)。

出発資料は「次数1・2・4の del Pezzo manifold 上の Poisson 構造と非可換幾何」、2026-11-11 v2.0、`del_Pezzo_1_2_4_Poisson_quantization_20261111_v2.pdf`（表紙を含む30頁）。次数1・2の §§1–9の内容は現行TeXへ統合済みである。旧PDFの複製や変更履歴を現行ツリーに置かず、研究を再開するのに必要な内容は現行ソースへ移した。次数4は比較に必要な内容を別ノートに整理し、詳細分類の正本を関連repoに置く。

数学的な点検、厳密検算、組版はそれぞれ別の検証である。現在の実行結果と再現方法は [docs/reproduction.md](../docs/reproduction.md)。未解決問題や未確認の優先権を、生成・組版の成功によって解決済みとはしない。
