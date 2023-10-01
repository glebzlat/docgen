(def left-margin 0)
(def right-margin 0)

(def box-width 50)

(defattrs :bg-green {:fill "#a0ffa0"})
(defattrs :bg-pink {:fill "#ffb0a0"})

(defn draw-header
  [span label]
  (draw-box (text label [:math {:font-size 12}]) {
                                                  :span span
                                                  :borders #{}
                                                  :height 14}))


(draw-header 1 "0")
(draw-header 1 "1")
(draw-header 1 "2")
(draw-header 1 "3")
(draw-header 1 "4")
(draw-header 5 "Next N bytes")
(draw-header 1 "N+5")
(next-row 18)

(draw-box "Addr" [{:span 1} :bg-green])
(draw-box "ID" [{:span 1} :bg-green])
(draw-box "Type" [{:span 2} :bg-green])
(draw-box "N" [{:span 1} :bg-green])
(draw-box "Payload" {:span 4 :borders #{:left :top :bottom}})
(draw-gap-inline)
(draw-box "CRC" [:bg-pink])
