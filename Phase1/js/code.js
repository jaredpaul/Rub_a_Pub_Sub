function test() {
  YUI().use(
    'aui-ace-editor',
    function(Y) {
      new Y.AceEditor(
        {
          boundingBox: '#myEditor',
          mode: 'python'
        }
      ).render();
    }
  );
}
