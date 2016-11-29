[Write a brief explanation about how your code works here!]
まず始めに,checkAdditionalMonth関数で入力として与えられた日付の年がremainder daysの影響で
通常より月数が多くなるかの判定を行っている.判定を行った結果trueが返されればargvより渡された年の月数を示す"monthsInYear"の
値を1つ増やす.
その後,getPastDays関数で基準となる”0001-01-01”からの経過日数を求め,daysInWeekで割った余りが曜日となる.
