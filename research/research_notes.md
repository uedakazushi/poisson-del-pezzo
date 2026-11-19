# 研究ノート：次数1・2と del Pezzo Poisson 構造

2026-11-20（JST） / v1.2

このノートは現行の数学的知識と次の着手方法をまとめる。完全な証明は [論文](../poisson-del-pezzo.tex) に置き、ここでは依存関係と論文外の課題を補う。[研究方針](../00_research_plan.md) を先に読む。

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

### モジュライと残る問題

$$
\mathcal D_{n,d}=[U_d/G_d],\qquad
\mathcal P_{n,d}=[(U_d\times\mathfrak C_{d,n})/G_d],
$$

ここで $\mathfrak C_{1,n}=\mathbb A^n$、$\mathfrak C_{2,n}=\operatorname{Cone}\operatorname{Gr}(2,n+1)$。実際の線束とその同型を記憶するスタックには $\widetilde G_d$ を使う。この非 rigid なスタックには $\mathbb G_m$ の自己同型が残り、DM とは呼ばない。

$H^0(T_X)=0$ は、重み0の接ベクトル場を Euler 方向で補正し、偏微分の Koszul syzygy の係数次数 $w_i+w_j-m<0$ を使うことで証明する。有限 stabilizer と商表示から rigid 化したスタックは DM となる。忘却射は affine、有限表示、平坦。完全な定義と証明は `sec:moduli`。

基本偏極のクラスは、相対 Picard 層の étale 性と各ファイバーの Picard 群の torsion-free 性により、無標識の滑らかな del Pezzo 族にも一意に定まる。従って $\mathcal D_{n,d}$ は無標識の多様体のモジュライとも同値である。実際の基本線束を大域的に選べるとは限らない。証明は `lemma:fundamental-polarization-class`。

スタックへの幾何学的点 $[X]\to\mathcal D_{n,d}$ に沿うファイバーは $\operatorname{Pois}_{\mathrm{sch}}(X)$ 自身である。$X$ の同型類だけを固定して自己同型も残すスタック $[\operatorname{Pois}_{\mathrm{sch}}(X)/\operatorname{Aut}(X,[H])]$ とは異なる。二重被覆 involution は $\pi$ と $-\pi$ を同型にするが、非零 $\pi$ を固定しない。射影化後はこの差が消える。

次数2、$n\geq3$ で非滑らかな点の集合が零切断に等しいという結果は **スタック**についてである。$n=2$ では全体が滑らかである。特異部分スキームが被約であることや coarse space の特異点を同定したことを意味しない。有限 stabilizer から separatedness や具体的 coarse space を無条件に推測しない。

## 4. 零 Poisson 切断の blow-up とその後の研究

次数2の $\mathcal P_{n,2}$ は、零点で Plücker 錐の特異性を持つ。$m=n+1$ とすると、頂点の埋め込み次元 $\binom m2$、錐次元 $2m-3$、余次元 $(m-2)(m-3)/2$。Plücker 二次関係の最小本数 $\binom m4$ と余次元の比較により、$n=3$ では通常の二次超曲面特異点、$n\ge4$ では非 lci が従う。

零切断 blow-up は相対 $\Gr(2,m)$ 上の $\mathcal O(-1)$ の全空間であり、$G_2$ の作用と同変なので商スタックへ降下する。例外因子は相対 Grassmann、法線束は $\mathcal O(-1)$。$K_{\Gr(2,m)}=\mathcal O(-m)$ と Plücker 環の既知の normal/ACM 性を用いると canonical module は $R(-m)$。零点の discrepancy は $m-1=n$ で、錐は Gorenstein terminal。証明は論文 `sec:singularities` にあり、このノートには重複させない。

研究上の残る焦点：この標準的解消を使った coarse moduli の局所商、自己同型群が増える層と例外因子の関係、特異 del Pezzo の境界上での吹き上げの比較。terminal の主張はアトラスの錐についてであり、有限群商の coarse space に自動的には移らない。

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
