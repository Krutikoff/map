import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0
import QtQuick.Layouts 1.13
import QtQuick.Dialogs 1.0



ApplicationWindow {
    visible: true
    width: 400
    height: 300
    Material.accent: Material.Blue

    Slider {
        value: 0.5
        x: 0
        y: 100
    }
    Column {
        x: 200
        y: 100
       
        
        RadioButton { text: qsTr("Small") }
        RadioButton { text: qsTr("Medium");  checked: true }
        RadioButton { text: qsTr("Large") }
        
    }

    RowLayout {
        
        Button {
            id: play_button
            objectName: "PlayButton" 
            text: "Play"
            
        }
        
        Button {
            objectName: "CancelButton"
            text: "Cancel" 

        }

        Button {
            id: fdialog
            objectName: "FileLoadButton"
            text: "File Load Button"
            
            signal file_dialog

            onClicked: {
                console.log("onClicked")
                fileDialogLoad.open()
            }
        }

        FileDialog {
                id: fileDialogLoad
                objectName: "FileDialog"
                title: "Please choose a file"
                folder: "file:///E:"
                property var aNumber: 100
                signal messageRequired(string person)
                onAccepted: {
                    
                    var path = fileDialogLoad.fileUrls
                    console.log("You chose: " + fileDialogLoad.fileUrls)
                    messageRequired(fileDialogLoad.fileUrls)
                    
                }

               
        }

    }
    
}