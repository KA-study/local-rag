# 2026/07/08 - UserConfigについて。

## 結論
一旦、UserConfigを使用不可能とする。

## 詳細
EditTreeは、ComponentsとUserConfigの両方に対応するように設計したつもりであった。
しかし、試験的に動作させたことで、実際には対応できていないことが発覚した。
これの修正作業はそこそこの時間を要することも明らかである。
加えて、UserConfigは、現在ほとんど使われておらず、重要度の低いものである。
したがって、一次的にUserConfigを使用不可能とし、EditTreeをComponents専用のクラスとする。

---

# 2026/07/06 - switch_user およびcreate_userの変更

## 結論
interface_adapterの上、ProfileServiceクラスに、switch_userメソッド及びcreate_suerメソッドを作成する。

## 理由
creat_userは、ほかのクラスからアクセスする機会もある。また、それぞれについて追加の機能を加えようとすると、その上の一般的に公開されているProfileServiceクラスに入り口を設けるべきである。

---

# 2026/07/01 - new user idの登録

## 結論
new user idの登録は、select_userにおいて、新規作成が選択されたときに、処理をProfileServiceまで上げる。

## 詳細
SessionManagerにおいて、new sessionが作られるとき、session_idを決定するだけでよかった。
そのため、ここではSessionManagerInterfaceAdapterにてnew session作成の処理を行っていた。
しかし、new user idの作成には、AppContext初期化などの、他のモジュールと連携する処理が伴う。
そのため、フラグを用いてProfileServiceまで処理を上げる。

---

# 2026/06/21 - _check_exitメソッドの廃止と統合

## 結論
- 各interfaceに実装していた_check_exitメソッドを廃止する。
- すべてのinterfaceのrootにInterfaceクラスを設定し、Interfaceに@finalで_inputメソッドを実装する。

## 詳細
_inputメソッドは、引数をそのままinputに渡し、その戻り値が:q（当プログラム全体での共通ExitCommand）であるかを判定し、
- :qでないならばそのまま戻り値としてinputの戻り値を戻す。
- :qならばExitCommandErrorを送出する。
このExitCommandErrorは、そのループブロックでハンドリングする。

---

# 2026/06/19 - EditComponentsInterface設計

## 結論
get_inputとdisplay_listを廃止し、select_changeを実装する。

## 理由
主に、GUIとCLIの実行方法の差を埋めるためである。
CLIは同期的に動くため、出力と入力を分離することができる。対して、
GUIはまずエンティティを表示し、入力を待機する。そして、入力があってから、処理が実行される。
すなわち、出力と入力がひとつながり、ということである。
GUIに対応させるため、出力と入力がひとつながりになるようにするため、get_inputとdisplay_listを廃止し、select_changeを実装する。

---

# 2026/06/18 - ComponentsかComponentか

## 結論
Componentsのままにする。

## 詳細
Componentは、言葉の意味を考えると、ComponentsではなくComponentとするべきである。
しかしながら、当プロジェクトにおけるComponentsは複数の差し替え可能クラスを保持することを強調したいため、複数形とする。

---

# 2026/06/16 - Interfaceのプリミティブ限定の部分的解除

## 結論
Interfaceでの引数、戻り値にDTOを使用することは禁止するが、特に用意したオブジェクトを使用することは許可する。

## 理由
edit_componets_interfaceのdisplay_listを構築する上で、プリミティブ型の実では限界があることがわかった。
したがって、引数と戻り値にDTOを直接使用することは禁ずるものの、それ専用に作り替えたオブジェクトを使用することは可能とする。

なお、DTOを禁止する理由は以下のとおりである。

DTOは、その範囲においてのみ有効なローカルなユーザー定義オブジェクトを含みうる。
処理層とinterfaceはprogram_files最上層でつながっているため、ローカルなユーザー定義オブジェクトをinterfaceに渡すことは、推奨されない。

---

# 2026/06/13 - Interfaceの実装方法

## 結論
entry pointによって決定されたInterfaceクラスは、その時点でグローバル変数としてインスタンス化する。

## 理由
Interfaceはプログラムの広範囲からのアクセスが考えられる。
それぞれ必要な部分にまで引数として渡していくと、Interfaceを必要としない中間層がInterfaceを持ってしまうことになる。
また、Interfaceはほかの機能とは性質が異なる、特別な機能でもある。
したがって、これはグローバル変数として、最初にインスタンス化し、どこからでもアクセスできる様にすることとした。

---

# 2026/06/12 - Interfaceクラス差し替え機能の分離

## 結論
Interfaceは他のcomponentsとは分離して実装する

## 理由
Componentsの変更には、Interfaceが必要である。
したがって、Interfaceはプログラム実行時にはすでに決定されていなければならない。
そのため、Interfaceごとにプログラム全体のentry pointを作り、それによって用いるInterfaceを変更する。
Interfaceはuser_idに依存しない。

---

# 2026/06/11 - AppContextの一意的存在の保証

## 結論
AppContextは、メソッドを持つ完全クラス、AppStateとして実装する。

## 理由
AppContextは、プログラム全体で、「常に」「ただ一つ」存在しなければならない。
AppContextとその編集メソッドを別々に実装したときのことを考える。
この時、「常に」「ただ一つ」存在することを保証するためには、その編集メソッドを扱うコード、
すなわちプログラムの最上層におけるコードが、編集メソッドの内部構造を完全に理解し、
AppContextの存在状態が条件を満たすことを確実にするため、細心の注意を払う必要がある。

これを避けるため、AppCotnextを自身を編集するメソッドを持つクラス、AppStateとして実装し、カプセル化する。

---

# 2026/06/06 - Cli/Guiの切り替え

## 結論
いまだに答えが出せないため、変更しやすいようにだけ意識し、仮組する。

## 詳細
cliとguiは、そもそも動作方式が異なるため、差し替えるだけでそれぞれを切り替えられるようにするのは、簡単ではない。
また、それに加えて、ChatInterfaceや、SessionManagerInterfaceのように、各ブロックについてクラスを分けている。
そのため、上層で一括でGUIとCLIを切り替えるのが容易ではなく、保守性の低い構造となってしまっている。

## 解決案
ひとまずcliとguiの一括切り替えを可能とするために、それぞれのinterfaceクラスを統括するAppInterfaceクラスなどを作る。

---

# 2026/06/06 - SessionContextの寿命、interfaceの取り決め

## 結論
- active.session.manager.pyにおいては、原則としてSessionContextを用いる。
- interface/の中では、このようなユーザー定義クラスを用いず、既存のクラスのみをもちいる。
上記二つの条件を満たすために、必要に応じて中間層を実装する。

## 理由
interface層にまでSessinoContextなどを回してしまうと、より広域にこれらのオブジェクトが影響することになる。
それぞれのオブジェクトの影響範囲は小さいほうがよいが、一方でstrなどの既存クラスを用いてしまうと、ご代入などを防げない。
したがって、処理層では(active層など)ユーザー定義dataclass等を用い、interface層では既存クラスを用いることにする。
また、そのため、中間層を必要に応じて実装する。

---

# 2026/06/04 - session_idの実装

## 結論
session_id(sessionを管理するdataclass)を追加し、またそれによってsessionを管理できるようにする。

## 詳細
session_idに従って、用いるhistoryなどを変更する。

---

# 2026/06/04 - chatブロックのデータ形式

## 結論
chatブロックを、strではなくMessage型オブジェクトとして扱う

## 理由
チャットテキストをstrで扱うと、その文章がLLMが生成したものか、userが入力したものかがわかりにくくなる。
したがって、strではなく、dataclass: Message　という形でその文章の持ち主を結び付け、扱う。

---

# 2026/06/02 - 複数userでのプログラムの使用

## 結論
現在は単一のuserが使うことにしか対応していないが、今後複数のuserが使うことに対応させる。

## 詳細
現在、単一のuserにのみ対応している。すなわち、cost管理や、使用するapi keyなどはuserによって切り替えられるようになっていない。
しかし、api keyをuserに合わせて自動的に変更し、cost管理もあるuserの分だけをlogから抽出する（またはuserごとにlogテーブルを作成する・primary keyをuser名にする）。
こうすることで、複数のuserに対応させることが可能である。
現状、current_statusテーブルのみが複数userの使用に対応している

---

# 2026/06/02 - SQliteUsageDBのdb設計

## 結論
今後、current_statusテーブルを、現状のみの記録およびその更新という形態から、累積型のlog型に変えるのがよいかもしれない。

## 理由
現状は、今その時の累積地のみを保存し、usage_logテーブルにその一回のusageを記録するたびにcurrent_statusを更新するよいう設計になっている。
しかし、current_statusは、usage_logがあるとはいえ、現在の値になるまでの道筋がまったく見えない。
したがって、現状のみを記録するのではなく、そこまでの毎回の累積値を残すlog型にするのがよいと考えられる。

---

# 2026/06/02 - top_kの管理

## 結論
top_kを指定する層を、より上層に移動させるべきである。

## 理由
現在、top_kはcreate_embedded_chunks()の中にしまわれている。
そのため、より上層からtop_kを認識できず、また変更できず、また利用できない。
したがって、より上層から引数として渡していく形に変更することで、利用しやすくし、一貫性を高めるべきである。

---

# 2026/06/01 - embeddingデータ型の切り替え

## 結論
embeddingの型を、VectorStoreの外ではnumpy.darray、VectorStoreの中ではlist[float]型として扱う。

## 注意
そのために、VectorStoreを呼び出す前に、numpy.darray型を.tolist()で変換するステップを踏むこと。

## コメント
今後、VectorStoreクラスに、numpy.darrayからlist[float]への変換を担当するメソッドを追加してもよいかもしれない。

---

# 2026/06/01 - クラス/protocolの呼び出し側実装

## 結論
簡略的に、クラス/protocol実装時は、引数として持たずに固定指定とする。

## 詳細
本来、クラス/protocol実装時は、それらを引数に指定することで、より上位の層ですべてのクラス/protocolを選択できるようにすべきである。
しかし、開発段階では、データフローの複雑性をできる限り減らすために、呼び出し時に直接具体クラスを呼び出すことにする。

---

# 2026/06/01 - クラス定義とprotocol

## 結論
現在混濁している、機能のクラス化とprotocol化の使い分けを整理する必要がある。

## 詳細
開発初期段階では、差し替え可能性のある関数などをすべてクラス化してきた。しかし、内部状態の保持などを目的に持たない場合は、protocolで実装したほうがよいということがわかった。
可能なときに、内部状態の保持を必要としない状態で実装されているクラスをprotocloに差し替える。
