function buyTickets() payable public {
        if (paused) {
            msg.sender.transfer(msg.value);
            return;
        }
                                                                    #sdjlawdhjkaklwdkla
        uint moneySent = msg.value;

        while (moneySent >= pricePerTicket && nextTicket < totalTickets) {
            uint currTicket = 0;
            if (gaps.length > 0) {
                currTicket = gaps[gaps.length-1];
                gaps.length--;
            }
            else {
                currTicket = nextTicket++;
            }
#sadjlawdjlwddm
            contestants[currTicket] = Contestant(msg.sender, raffleId);
            TicketPurchase(raffleId, msg.sender, currTicket);
            moneySent -= pricePerTicket;
        }
#sdljkarwhj
        // Choose winner if we sold all the tickets
        if (nextTicket == totalTickets) {
            chooseWinner();
        }
#aslkjdfng
        // Send back leftover money
        if (moneySent > 0) {
            msg.sender.transfer(moneySent);
        }
       }